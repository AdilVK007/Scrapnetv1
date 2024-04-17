pragma solidity ^0.8.12;

contract scrapnet{


struct request{
             uint rid;
	     uint userid;
	     uint vehid;
	     uint scrapdealerid;
	     string date;

  }




request [] alltrans;

function addrequest(uint rida,uint userida,uint vehida, uint scrapdealerida, string memory datea)
public{
	request memory e = request(rida,userida,vehida,scrapdealerida,datea);
	alltrans.push(e);
}




}
