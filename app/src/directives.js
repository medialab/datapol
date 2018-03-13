'use strict';

/* Services */

angular.module('app.directives', [])

	.directive('infoDataset', ['datasets', '$mdDialog', function(datasets, $mdDialog){
    return {
      restrict: 'A'
      ,templateUrl: 'src/info-dataset.html'
      ,scope: {
      }
      ,transclude: true
      ,link: function($scope, el, attrs, ctrl, transclude) {
        
        $scope.openDialog = function(ev) {
        	var dataset = datasets.get(attrs.infoDataset)
        	console.log(dataset)
        	$mdDialog.show(
			      $mdDialog.alert()
			        .clickOutsideToClose(true)
			        .title(dataset.title)
			        .htmlContent(
			        		'' + dataset.description + '<br><br><span class="md-body-2">Licence : ' + dataset.licence + '</span>'
			        	)
			        .ok('ok')
			        .targetEvent(ev)
			    );
       	}

       	transclude($scope, function(clone) {
          $scope.originalExpression = clone[0].textContent
       	});
        

      }
    }
  }])

