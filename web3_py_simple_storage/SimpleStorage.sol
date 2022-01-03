// SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 < 0.9.0;

contract SimpleStorage {
    //if not initialized, will get null value
    uint256 favoriteNumber;
    //bool favoriteBool=true;
    //string favoriteString="String";
    //address favoriteAddress=0xA8c831b070dACb2af8BAFbd7Cda072CeE22594D8;
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping (string=>uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber=_favoriteNumber;
    }
    function getFavoriteNumber() public view returns(uint256){
        return favoriteNumber;
    }
    function addPerson(string memory _name,uint256 _favoriteNumber)public {
        people.push(People({favoriteNumber:_favoriteNumber,name:_name}));
        nameToFavoriteNumber[_name]=_favoriteNumber;
    }
}