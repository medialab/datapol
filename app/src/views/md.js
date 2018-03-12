'use strict';

angular.module('app.md', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/', {
    templateUrl: 'src/views/md.html'
  , controller: 'MarkdownController'
  })
}])

.controller('MarkdownController', function(
	$scope,
	$location,
	$timeout,
	$routeParams
) {
	
	
})
