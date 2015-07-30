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
        $scope.open = function (personneId){
            var modalInstance = $modal.open({
                animation: true,
                templateUrl: '/static/personnel/app/partials/personne-detail.html',
                controller: 'PersonneCtrl',
                size: 'sm',
                resolve: {
                    id: function(){
                        return personneId;
                    }
                }

            })
        }

    }]);

servicesControlers.controller('PersonneCtrl', ['$scope',  '$modalInstance',  'Personnel', 'id',
    function ($scope,  $modalInstance, Personnel, id) {
        console.log(id);
        $scope.personne = Personnel.personne_ressource().get({personnelId: id});
        $scope.ok = function () {
            $modalInstance.close();
          };
        $scope.cancel = function () {
            $modalInstance.dismiss('cancel');
          };
    }]);