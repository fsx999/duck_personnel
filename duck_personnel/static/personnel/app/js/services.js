/**
 * Created by paulguichon on 29/07/2015.
 */
var servicesServices = angular.module('servicesServices', ['ngResource']);

servicesServices.factory('Service', ['$resource',
    function ($resource) {

        return $resource('/personnel/services/:serviceId', {}, {
            query: {method: 'GET', params: {serviceId: '@serviceId'}, isArray: true}

        });
    }]);

servicesServices.factory('Personnel',['$http', '$resource',
    function($http, $resource){
        var personne_by_service = function(service){
                     return $http.get('/personnel/personnels', {params: {service: service.id}, isArray: true}).success(function(data){
                         service.personnes = data;
                     });
        };
        var personne_ressouce = function(){
            return $resource('/personnel/personnels/:personnelId', {personnelId:'@id'}, {"update": {method: "PUT"}})
        };
        return {personne_by_service: personne_by_service, personne_ressource: personne_ressouce}
    }]);