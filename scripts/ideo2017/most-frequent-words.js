const request = require('request'),
      async = require('async'),
      mkdirp = require('mkdirp'),
      cheerio = require('cheerio'),
      artoo = require('artoo-js'),
      path = require('path'),
      fs = require('fs');

const candidates = require('./candidates');

const url = candidate => `http://patrimeph.ensea.fr/RST/iramu.php?CorpusName=Corpus%2F${candidate}.txt&candidat=${candidate}&stat=`;

async.mapSeries(candidates, (candidate, next) => {

  console.log(`Processing ${candidate}...`);
  request(url(candidate), (err, response, body) => {
    if (err)
      return next(err);

    const $ = cheerio.load(body);
    artoo.setContext($);

    const table = artoo
      .scrapeTable('table.table-bordered')
      .slice(1)
      .map(row => {
        return {
          word: row[0],
          frequency: row[1],
          type: row[2]
        };
      });

    return next(null, table);
  });
}, (err, data) => {
  if (err)
    return console.error(err);

  const folder = path.join('.output', 'most-frequent-words');

  mkdirp.sync(folder);

  data.forEach((candidateData, i) => {
    fs.writeFileSync(path.join(folder, `${candidates[i]}.csv`), artoo.writers.csv(candidateData));
  });
});
