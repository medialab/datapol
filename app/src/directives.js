'use strict';

/* Services */

angular.module('app.directives', [])

	.directive('infoDataset', ['datasets', function(datasets){
    return {
      restrict: 'A'
      ,templateUrl: 'src/info-dataset.html'
      ,scope: {
      }
      ,transclude: true
      ,link: function($scope, el, attrs, ctrl, transclude) {
        
        $scope.openDialog = function() {
        	alert(attrs.infoDataset)
        	console.log('attrs', attrs)
       	}

       	transclude($scope, function(clone) {
          $scope.originalExpression = clone[0].textContent
       	});
        

      }
    }
  }])

