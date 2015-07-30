/**
 * Created by paulguichon on 29/07/2015.
 */

var servicesControlers = angular.module('servicesControlers', []);

servicesControlers.controller('ServiceListCtrl', ['$scope', '$http', '$q', 'Service', 'Personnel',
    function ($scope, $http, $q, Service, Personnel) {

        Service.query(function(data){
            $scope.services = data;

            for (index = 0, len = data.length; index < len; ++index) {
                s = data[index];
                 Personnel.personne_by_service(s);

            }
            console.log($scope.services);
        });

    }]);