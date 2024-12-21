var senderAddress = "0xb5d83AC8B1d4829FF68844DA34Fe9E7778a6D06B";
var receiverAddress = "0x572fdAD8DB65b28500987c194e9A5f49655Fd431";

var amountToSend = web3.toWei(0.01711, "ether"); 
var password = "rahasia";
personal.unlockAccount(senderAddress, password, 15000);

var tx = {
    from: senderAddress,
    to: receiverAddress,
    value: amountToSend,
    gas: 21000, // Standard gas limit for a simple transfer
    gasPrice: web3.toWei('20', 'gwei') // Gas price (in Wei)
};
var txHash = eth.sendTransaction(tx);
console.log("Transaction hash: " + txHash);