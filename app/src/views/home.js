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
		{
			name: 'médialab de Sciences Po',
			logo: 'res/medialab.svg',
			link: 'http://www.medialab.sciences-po.fr'
		},{
			name: 'CEVIPOF',
			logo: 'res/cevipof.svg',
			link: 'http://www.cevipof.com/'
		},{
			name: 'Institut des Systèmes Complexes',
			logo: 'res/ISCPIF.svg',
			link: 'https://iscpif.fr/'
		},{
			name: 'Public Data Lab',
			logo: 'res/pdl.svg',
			link: 'http://publicdatalab.org/'
		},{
			name: 'Linkfluence',
			logo: 'res/linkfluence.svg',
			link: 'https://linkfluence.com/'
		},{
			name: 'Les Décodeurs',
			logo: 'res/decodeurs.svg',
			link: 'http://lemonde.fr/les-decodeurs/'
		}
	]
	
})
