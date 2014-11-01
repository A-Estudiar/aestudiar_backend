'use strict';

describe('Controller: PuntuarCtrl', function () {

  // load the controller's module
  beforeEach(module('aestudiarApp'));

  var PuntuarCtrl,
    scope;

  // Initialize the controller and a mock scope
  beforeEach(inject(function ($controller, $rootScope) {
    scope = $rootScope.$new();
    PuntuarCtrl = $controller('PuntuarCtrl', {
      $scope: scope
    });
  }));

  it('should attach a list of awesomeThings to the scope', function () {
    expect(scope.awesomeThings.length).toBe(3);
  });
});
