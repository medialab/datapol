const request = require('request'),
      async = require('async'),
      mkdirp = require('mkdirp'),
      cheerio = require('cheerio'),
      artoo = require('artoo-js'),
      path = require('path'),
      fs = require('fs');

const MultiSet = require('mnemonist/multi-set'),
      MultiMap = require('mnemonist/multi-map');

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
          frequency: +row[1],
          type: row[2]
        };
      });

    return next(null, table);
  });
}, (err, data) => {
  if (err)
    return console.error(err);

  const words = new MultiSet(),
        wordsToCandidates = new MultiMap(),
        types = new Map();

  data.forEach((candidateData, i) => {
    candidateData.forEach(row => {
      types.set(row.word, row.type);
      words.add(row.word, row.frequency);
      wordsToCandidates.set(row.word, candidates[i]);
    });
  });

  const aggregated = Array.from(types.keys()).map(word => {
    return {
      word,
      frequency: words.multiplicity(word),
      candidatesCount: wordsToCandidates.multiplicity(word),
      candidates: wordsToCandidates.get(word).join('|'),
      type: types.get(word)
    };
  });

  const folder = path.join('.output', 'most-frequent-words');

  mkdirp.sync(folder);

  fs.writeFileSync(path.join(folder, `aggregated.csv`), artoo.writers.csv(aggregated));

  data.forEach((candidateData, i) => {
    fs.writeFileSync(path.join(folder, `${candidates[i]}.csv`), artoo.writers.csv(candidateData));
  });
});
