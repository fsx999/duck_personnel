/**
 * Created by paulguichon on 29/07/2015.
 */

var personnelApp = angular.module('personnelApp', []);

personnelApp.controller('ServiceListCtrl', ['$scope', '$http',
    function($scope, $http){
    $http.get('/personnel/services/').success(function(data){
         $scope.services = data;
    });


}]);