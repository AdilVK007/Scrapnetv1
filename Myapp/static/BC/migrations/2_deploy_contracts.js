var HelloWorld=artifacts.require ("scrapnet.sol");
module.exports = function(deployer) {
      deployer.deploy(HelloWorld);
}