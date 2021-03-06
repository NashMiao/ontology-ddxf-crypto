# Ontology DDXF Cryptography Components

English | [中文](README_CN.md)

<!-- TOC -->

- [1. Preparations](#1-preparations)
- [2. Ontology Distributed Identity Framework (ONT ID)](#2-ontology-distributed-identity-framework-ont-id)
- [3. Encryption Service Based on ONT ID](#3-encryption-service-based-on-ont-id)
    - [3.1. Encryption Process](#31-encryption-process)
    - [3.2. Decryption Process](#32-decryption-process)
- [4. Password-Based Key Derivation Function (PBKDF)](#4-password-based-key-derivation-function-pbkdf)
- [5. Elliptic Curve Integrated Encryption Scheme (ECIES)](#5-elliptic-curve-integrated-encryption-scheme-ecies)

<!-- /TOC -->

## 1. Preparations

Installation requires a Python 3.5 or later environment.

```shell
pip install ontology-ddxf-crypto
```

## 2. Ontology Distributed Identity Framework (ONT ID)

Ontology DID (also called ONT ID) is a decentralized identity identification protocol based on W3C DID specifications. ONT ID establishes a cryptographically-based digital identity for each entity, allowing self-sovereign of data authorization and ownership confirmation, which makes the identity and data truly assets that the user can control.

If you are interested in ONT ID, you can find a detailed introduction [here](https://ontio.github.io/documentation/ontology_DID_en.html).

<div align=center><img height="400" src="img/ontid.jpg"/></div>

## 3. Encryption Service Based on ONT ID

### 3.1. Encryption Process

There are three main steps to encrypting data:

- Query public key: Access the smart contract in the ontology blockchain and get the corresponding public key `pk` based on the data requester's `ONT ID`.
- Random sampling: Randomly sample 256-bit data to obtain the Advanced Encryption Standard (AES) key `key`.
- Encryption: The AES256 key is encrypted using the Public Key Encryption Algorithm (PKE) to get `ekey`, and the plaintext data `m` is encrypted using AES256-GCM to get the ciphertext data `c`.

<div align=center><img width="500" src="img/endToEnd.png"/></div>

### 3.2. Decryption Process

- Query private key: Find the corresponding private key `sk` from the private key management module according to `ONT ID` and `PKIndex`.
- Decrypt symmetric key: Use the private key `sk` to decrypt the encrypted key `ekey` to get the AES symmetric key `key`.
- Decrypt data: Use the AES symmetric key `key` to decrypt the ciphertext data `c` to get the plaintext data `m`.

## 4. Password-Based Key Derivation Function (PBKDF)

In cryptography, PBKDF (Password-Based Key Derivation Function) is key derivation functions with a sliding computational cost, aimed to reduce the vulnerability of encrypted keys to brute force attacks.

In Distributed Data eXchange Framework(short for DDXF), the hash function used by the key derivation algorithm is `SHA256`, and algorithm is as follows:

- Input: `seed`, derived key length `dkLen` (in bits).
- Output: Derived key `key` of length `dklen`.

```python
def pbkdf2(seed: str or bytes, dk_len: int) -> bytes:
    key = b''
    index = 1
    bytes_seed = str_to_bytes(seed)
    while len(key) < dk_len:
        key += sha256(b''.join([bytes_seed, int_to_little_bytes(index)]))
        index += 1
    return key[:dk_len]
```

## 5. Elliptic Curve Integrated Encryption Scheme (ECIES)

Elliptic Curve Integrated Encryption Scheme(also ECIES), is a hybrid encryption system proposed by Victor Shoup in 2001. Shoup's submission can be found at [here](https://www.shoup.net/papers/iso-2_1.pdf).
