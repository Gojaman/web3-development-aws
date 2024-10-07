var FundProjectForOwner = artifacts.require("./FundProjectForOwner.sol");

module.exports = function(deployer) {
    deployer.deploy(FundProjectForOwner);
};