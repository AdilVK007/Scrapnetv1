pragma solidity ^0.8.12;

contract scrapnet{


struct request{
             uint reqid;
	     uint lida;
	     uint vehicleid;
	     string typea;
	     string date;
	     string status;

  }




request [] alltrans;

function addrequest(uint reqida,uint lida,uint vehicleida, string memory typea, string memory datea, string memory statusa)
public{
	request memory e = request(reqida,lida,vehicleida,typea,datea,statusa);
	alltrans.push(e);
}



}
