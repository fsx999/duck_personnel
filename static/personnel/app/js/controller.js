/**
 * Created by paulguichon on 29/07/2015.
 */

var servicesControlers = angular.module('servicesControlers', []);

servicesControlers.controller('ServiceListCtrl', ['$scope',  'Service', 'Personnel', '$modal',
    function ($scope,  Service, Personnel, $modal) {

        Service.query(function(data){
            $scope.services = data;

            for (index = 0, len = data.length; index < len; ++index) {
                s = data[index];
                 Personnel.personne_by_service(s);

            }
        });
        $scope.open = function (personne){
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: '/static/personnel/app/partials/personne-detail.html',
                controller: 'PersonneCtrl',
                size: 'sm',
                resolve: {
                    personne: function(){
                        return personne;
                    }
                }

            })
        }

    }]);

servicesControlers.controller('PersonneCtrl', ['$scope',  '$modalInstance', '$modal', 'Personnel', 'personne',
    function ($scope,  $modalInstance, $modal, Personnel, personne) {
        //$scope.personne = Personnel.personne_ressource().get({personnelId: id});
        $scope.personne = personne;
        $scope.ok = function () {
            $modalInstance.close();
          };
        $scope.edit = function () {
            $modalInstance.close();
            var modalInstance = $modal.open({
                animation: false,
                templateUrl: '/static/personnel/app/partials/personne-update.html',
                controller: 'PersonneUpdateCtrl',
                size: 'sm',
                resolve: {
                    personne: function(){
                        return personne;
                    }
                }

            })
          };

    }]);

servicesControlers.controller('PersonneUpdateCtrl', ['$scope',  '$modalInstance',  'Personnel', 'personne',
    function ($scope,  $modalInstance, Personnel, personne) {
        $scope.personne = personne;

        $scope.update = function(personne){
            Personnel.personne_ressource().update(personne, function(data){
                $scope.message = {type: 'success', message: 'Dossier bien modifié'}
            });
        };

        $scope.quit = function () {
            $modalInstance.close();
          };

    }]);