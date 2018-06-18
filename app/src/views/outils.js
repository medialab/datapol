'use strict';

angular.module('app.outils', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/outils/', {
    templateUrl: 'src/views/outils.html'
  , controller: 'OutilsController'
  })
}])

.controller('OutilsController', function(
	$scope
) {
})
