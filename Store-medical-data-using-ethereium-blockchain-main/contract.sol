// contracts/EscrowContract.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EscrowContract {
    address public owner;
    address public user;
    uint256 public ownerEscrow;
    uint256 public userEscrow;
    bool public ownerDeposited;
    bool public userDeposited;
    bool public transactionComplete;
    
    // Constructor to initialize owner and user addresses
    constructor(address _user) {
        owner = msg.sender;  // The deployer of the contract is the owner
        user = _user;
    }
    
    // Modifier to restrict function access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the owner");
        _;
    }
    
    // Modifier to restrict function access to user
    modifier onlyUser() {
        require(msg.sender == user, "Not the user");
        _;
    }
    
    // Deposit escrow by owner
    function depositOwnerEscrow() public payable onlyOwner {
        require(!ownerDeposited, "Owner already deposited");
        require(msg.value > 0, "Escrow amount must be greater than 0");
        ownerEscrow = msg.value;
        ownerDeposited = true;
    }
    
    // Deposit escrow by user
    function depositUserEscrow() public payable onlyUser {
        require(!userDeposited, "User already deposited");
        require(msg.value > 0, "Escrow amount must be greater than 0");
        userEscrow = msg.value;
        userDeposited = true;
    }
    
    // Mark transaction as complete (both parties agree)
    function completeTransaction() public {
        require(ownerDeposited && userDeposited, "Both parties must deposit escrow");
        require(!transactionComplete, "Transaction already completed");

        // Assuming a mutually agreed completion, both parties get their escrow back
        payable(owner).transfer(ownerEscrow);
        payable(user).transfer(userEscrow);
        
        transactionComplete = true;
    }
    
    // In case of a dispute, resolve by forfeiting escrow from the cheating party
    function resolveDispute(bool userCheated) public {
        require(ownerDeposited && userDeposited, "Both parties must deposit escrow");
        require(!transactionComplete, "Transaction already completed");

        if (userCheated) {
            // User forfeits escrow to owner
            payable(owner).transfer(ownerEscrow + userEscrow);
        } else {
            // Owner forfeits escrow to user
            payable(user).transfer(ownerEscrow + userEscrow);
        }
        
        transactionComplete = true;
    }
    
    // Withdraw escrow in case of cancelation
    function cancelTransaction() public {
        require(ownerDeposited && userDeposited, "Both parties must deposit escrow");
        require(!transactionComplete, "Transaction already completed");

        // If both agree to cancel, they can withdraw their funds back
        if (msg.sender == owner) {
            payable(owner).transfer(ownerEscrow);
            ownerEscrow = 0;
        } else if (msg.sender == user) {
            payable(user).transfer(userEscrow);
            userEscrow = 0;
        }
        
        ownerDeposited = false;
        userDeposited = false;
    }
}