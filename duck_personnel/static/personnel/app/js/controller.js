/**
 * Created by paulguichon on 29/07/2015.
 */

var servicesControlers = angular.module('servicesControlers', []);

servicesControlers.controller('ServiceListCtrl', ['$scope', '$http', '$q', 'Service',
    function ($scope, $http, $q, Service) {

        $scope.services = Service.query();
        $scope.service = Service




    }]);