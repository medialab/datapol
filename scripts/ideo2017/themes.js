const request = require('request'),
      async = require('async'),
      mkdirp = require('mkdirp'),
      cheerio = require('cheerio'),
      artoo = require('artoo-js'),
      path = require('path'),
      fs = require('fs');

const MultiMap = require('mnemonist/multi-map');

const candidates = require('./candidates');

const url = candidate => `http://patrimeph.ensea.fr/RST/iramu.php?CorpusName=Corpus%2F${candidate}.txt&candidat=${candidate}&alceste=`;

const headers = nbThemes => {
  return ['word']
    .concat(new Array(nbThemes).fill(0).map((_, i) => `theme${i + 1}`))
    .concat('themes');
};

const rawHeaders = nbThemes => (new Array(nbThemes).fill(0).map((_, i) => `theme${i + 1}`));

async.mapSeries(candidates, (candidate, next) => {

  console.log(`Processing ${candidate}...`);
  request(url(candidate), (err, response, body) => {
    if (err)
      return next(err);

    const $ = cheerio.load(body);
    artoo.setContext($);

    const themes = artoo.scrape('.table-title', function() {
      const $table = $(this).find('td');

      return artoo.scrape($table).filter(x => x);
    });

    return next(null, themes);
  });
}, (err, data) => {
  if (err)
    return console.error(err);

  const folder = path.join('.output', 'themes');

  mkdirp.sync(folder);

  data.forEach((themes, candidate) => {
    const maxLength = Math.max.apply(null, themes.map(d => d.length));

    const csvData = [rawHeaders(themes.length)]
      .concat((new Array(maxLength)).fill(0).map(() => []));

    themes.forEach((theme, i) => {
      theme.forEach((word, j) => {
        csvData[j + 1][i] = word;
      });
    });

    fs.writeFileSync(path.join(folder, `${candidates[candidate]}.raw.csv`), artoo.writers.csv(csvData));
  });

  data = data
    .map((themes, candidate) => {
      const map = new MultiMap();

      themes.forEach((words, theme) => {
        words.forEach(word => (map.set(word, theme)));
      });

      const csvData = [headers(themes.length)];

      Array.from(map.associations()).forEach(([word, themes]) => {
        const row = [
          word,
          '',
          '',
          '',
          '',
          '',
          '',
          themes.join('|')
        ];

        themes.forEach(theme => (row[theme + 1] = 'x'));

        csvData.push(row);
      });

      return csvData;
    });

  data.forEach((candidateData, i) => {
    fs.writeFileSync(path.join(folder, `${candidates[i]}.csv`), artoo.writers.csv(candidateData));
  });
});
