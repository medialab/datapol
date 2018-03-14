'use strict';

angular.module('app.datasets', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/datasets/:dataset', {
    templateUrl: 'src/views/datasets.html'
  , controller: 'DatasetController'
  })
  .when('/datasets/', {
    templateUrl: 'src/views/datasets.html'
  , controller: 'DatasetController'
  })
}])

.controller('DatasetController', function(
	$scope,
	$location,
	$timeout,
	$routeParams,
	datasets
) {
	
	$scope.datasets = datasets.getAll({sort:'licence'})
	
})
