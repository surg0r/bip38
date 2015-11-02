# bip38

Python 2.7 BIP38 paper wallet creator

A quick and dirty script using libraries: bip38, PIL and bitcoin.

It is a commandline script which either generates a fresh random private key or accepts a user-supplied key, then
creates a jpg with a bitcoin address and a bip38 address with corresponding QR codes (with error protection) painted
on it.

BIP38 is a protocol which encrypts a bitcoin private key with a pass phrase (using AES and scrypt) such that
brute forcing will be very difficult / time consuming. Thus it is an elegant form of 2-factor on a bitcoin paper 
wallet. The benefit is that the bitcoin funds are not at major risk if the key is found, whilst also being easily
imported into a variety of popular bitcoin wallets via a sweep of the QR code.

This script also allow user generated bip38 keys for user private keys to allow the code+address to be sent to 3rd
parties safely (for example to create a metal laser engraved wallet).

Issues:

1) probably should update the code to export a pdf file.
