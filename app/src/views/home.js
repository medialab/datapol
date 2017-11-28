'use strict';

angular.module('app.home', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: 'src/views/home.html'
  , controller: 'HomeController'
  })
}])

.controller('HomeController', function(
	$scope,
	$location,
	$timeout,
	$routeParams
) {
	$scope.organisateurs = [
		/*{
			name: 'médialab de Sciences Po',
			logo: 'res/medialab.svg',
			link: 'http://www.medialab.sciences-po.fr'
		},{
			name: 'CEVIPOF',
			logo: 'res/cevipof.svg',
			link: 'http://www.cevipof.com/'
		},{
			name: 'Ecole de Jouralisme de Sciences Po',
			logo: 'res/ecolejournalisme.svg',
			link: 'http://www.journalisme.sciences-po.fr/'
		},{
			name: 'Bibliothèque de Sciences Po',
			logo: 'res/spbib.svg',
			link: 'http://bibliotheque.sciences-po.fr'
		},*/{
			name: 'Sciences Po',
			logo: 'res/sciencespo.svg',
			link: 'https://sciences-po.fr/'
		},{
			name: 'Institut des Systèmes Complexes',
			logo: 'res/ISCPIF.svg',
			link: 'https://iscpif.fr/'
		},{
			name: 'Public Data Lab',
			logo: 'res/pdl.svg',
			link: 'http://publicdatalab.org/'
		},{
			name: 'INA',
			logo: 'res/INA.svg',
			link: 'http://www.ina.fr/'
		},{
			name: 'Linkfluence',
			logo: 'res/linkfluence.svg',
			link: 'https://linkfluence.com/'
		},{
			name: 'Les Décodeurs',
			logo: 'res/decodeurs.svg',
			link: 'http://lemonde.fr/les-decodeurs/'
		}/*,{
			name: 'Google News Lab',
			logo: 'res/googlenewslab.svg',
			link: 'https://newslab.withgoogle.com/'
		}*/,{
			name: 'Matlo',
			logo: 'res/matlo.svg',
			link: 'https://www.matlo.com/'
		}
	]
	
})
