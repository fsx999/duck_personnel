/**
 * Created by paulguichon on 29/07/2015.
 */
var servicesServices = angular.module('servicesServices', ['ngResource']);

servicesServices.factory('Service', ['$resource', '$q', '$http',
    function ($resource, $q, $http) {
            var personnes;
            var promiseStart = $q.when('start');
            var promise1 = promiseStart.then(function (value) {

                return $http.get('/personnel/personnels/?fonction__service=' + serviceId).success(function (data) {
                    personnes = data;
                });
            });

            var promiseEnd = promise1.then(function (value) {


                return {personnes: personnes};
            }, function (reason) {

                return $q.reject(reason);
            });
            return promiseEnd;
        return $resource('/personnel/services/:serviceId', {}, {
            query: {method: 'GET', params: {serviceId: ''}, isArray: true}

        });
    }]);