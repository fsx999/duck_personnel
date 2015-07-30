/**
 * Created by paulguichon on 29/07/2015.
 */
var servicesServices = angular.module('servicesServices', ['ngResource']);

servicesServices.factory('Service', ['$resource', '$q', '$http',
    function ($resource, $q, $http) {

        return $resource('/personnel/services/:serviceId', {}, {
            query: {method: 'GET', params: {serviceId: ''}, isArray: true}

        });
    }]);

servicesServices.factory('Personnel',['$http',
    function($http){
        var personne_by_service = function(service){
                     return $http.get('/personnel/personnels/', {params: {fonction__service: service.id}, isArray: true}).success(function(data){
                         service.personnes = data;
                     });

        };
        return {personne_by_service: personne_by_service}
    }]);