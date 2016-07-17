var app = angular.module('fteller-app', [])

app.controller('FtellerController', function($scope, $http) {
    $scope.questionval = ""

    $scope.question = function() {
        console.log($scope.questionval)

        $http({
            method: 'POST',
            data: $scope.questionval,
            url: "/question",
            success: function(response) {
                alert(response)
            }
        })
    }
})
