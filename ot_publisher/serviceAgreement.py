serviceAgreementABI = [
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "hubAddress",
        "type": "address"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "inputs": [],
    "name": "ScoreError",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint8",
        "name": "scoreFunctionId",
        "type": "uint8"
      }
    ],
    "name": "ScoreFunctionDoesntExist",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "TooLowAllowance",
    "type": "error"
  },
  {
    "inputs": [
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "TooLowBalance",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "ZeroEpochsNumber",
    "type": "error"
  },
  {
    "inputs": [],
    "name": "ZeroTokenAmount",
    "type": "error"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "address",
        "name": "assetContract",
        "type": "address"
      },
      {
        "indexed": True,
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "bytes",
        "name": "keyword",
        "type": "bytes"
      },
      {
        "indexed": False,
        "internalType": "uint8",
        "name": "hashFunctionId",
        "type": "uint8"
      },
      {
        "indexed": False,
        "internalType": "uint256",
        "name": "startTime",
        "type": "uint256"
      },
      {
        "indexed": False,
        "internalType": "uint16",
        "name": "epochsNumber",
        "type": "uint16"
      },
      {
        "indexed": False,
        "internalType": "uint128",
        "name": "epochLength",
        "type": "uint128"
      },
      {
        "indexed": False,
        "internalType": "uint96",
        "name": "tokenAmount",
        "type": "uint96"
      }
    ],
    "name": "ServiceAgreementV1Created",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "internalType": "uint16",
        "name": "epochsNumber",
        "type": "uint16"
      }
    ],
    "name": "ServiceAgreementV1Extended",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "internalType": "uint96",
        "name": "tokenAmount",
        "type": "uint96"
      }
    ],
    "name": "ServiceAgreementV1RewardRaised",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      }
    ],
    "name": "ServiceAgreementV1Terminated",
    "type": "event"
  },
  {
    "anonymous": False,
    "inputs": [
      {
        "indexed": True,
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "indexed": False,
        "internalType": "uint96",
        "name": "updateTokenAmount",
        "type": "uint96"
      }
    ],
    "name": "ServiceAgreementV1UpdateRewardRaised",
    "type": "event"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "assetOwner",
        "type": "address"
      },
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "internalType": "uint96",
        "name": "tokenAmount",
        "type": "uint96"
      }
    ],
    "name": "addTokens",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "assetOwner",
        "type": "address"
      },
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "internalType": "uint96",
        "name": "tokenAmount",
        "type": "uint96"
      }
    ],
    "name": "addUpdateTokens",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "commitManagerV1",
    "outputs": [
      {
        "internalType": "contract CommitManagerV1",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "commitManagerV1U1",
    "outputs": [
      {
        "internalType": "contract CommitManagerV1U1",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "assetCreator",
            "type": "address"
          },
          {
            "internalType": "address",
            "name": "assetContract",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "tokenId",
            "type": "uint256"
          },
          {
            "internalType": "bytes",
            "name": "keyword",
            "type": "bytes"
          },
          {
            "internalType": "uint8",
            "name": "hashFunctionId",
            "type": "uint8"
          },
          {
            "internalType": "uint16",
            "name": "epochsNumber",
            "type": "uint16"
          },
          {
            "internalType": "uint96",
            "name": "tokenAmount",
            "type": "uint96"
          },
          {
            "internalType": "uint8",
            "name": "scoreFunctionId",
            "type": "uint8"
          }
        ],
        "internalType": "struct ServiceAgreementStructsV1.ServiceAgreementInputArgs",
        "name": "args",
        "type": "tuple"
      }
    ],
    "name": "createServiceAgreement",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "assetOwner",
        "type": "address"
      },
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "internalType": "uint16",
        "name": "epochsNumber",
        "type": "uint16"
      },
      {
        "internalType": "uint96",
        "name": "tokenAmount",
        "type": "uint96"
      }
    ],
    "name": "extendStoringPeriod",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "sender",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "assetContract",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "tokenId",
        "type": "uint256"
      },
      {
        "internalType": "uint16",
        "name": "epoch",
        "type": "uint16"
      }
    ],
    "name": "getChallenge",
    "outputs": [
      {
        "internalType": "bytes32",
        "name": "assertionId",
        "type": "bytes32"
      },
      {
        "internalType": "uint256",
        "name": "challenge",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "internalType": "uint16",
        "name": "epoch",
        "type": "uint16"
      }
    ],
    "name": "getTopCommitSubmissions",
    "outputs": [
      {
        "components": [
          {
            "internalType": "uint72",
            "name": "identityId",
            "type": "uint72"
          },
          {
            "internalType": "uint72",
            "name": "prevIdentityId",
            "type": "uint72"
          },
          {
            "internalType": "uint72",
            "name": "nextIdentityId",
            "type": "uint72"
          },
          {
            "internalType": "uint40",
            "name": "score",
            "type": "uint40"
          }
        ],
        "internalType": "struct ServiceAgreementStructsV1.CommitSubmission[]",
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "hashingProxy",
    "outputs": [
      {
        "internalType": "contract HashingProxy",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "hub",
    "outputs": [
      {
        "internalType": "contract Hub",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "initialize",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "internalType": "uint16",
        "name": "epoch",
        "type": "uint16"
      }
    ],
    "name": "isCommitWindowOpen",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      },
      {
        "internalType": "uint16",
        "name": "epoch",
        "type": "uint16"
      }
    ],
    "name": "isProofWindowOpen",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "parametersStorage",
    "outputs": [
      {
        "internalType": "contract ParametersStorage",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "proofManagerV1",
    "outputs": [
      {
        "internalType": "contract ProofManagerV1",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "proofManagerV1U1",
    "outputs": [
      {
        "internalType": "contract ProofManagerV1U1",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "scoringProxy",
    "outputs": [
      {
        "internalType": "contract ScoringProxy",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "assetContract",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "tokenId",
            "type": "uint256"
          },
          {
            "internalType": "bytes",
            "name": "keyword",
            "type": "bytes"
          },
          {
            "internalType": "uint8",
            "name": "hashFunctionId",
            "type": "uint8"
          },
          {
            "internalType": "uint16",
            "name": "epoch",
            "type": "uint16"
          },
          {
            "internalType": "bytes32[]",
            "name": "proof",
            "type": "bytes32[]"
          },
          {
            "internalType": "bytes32",
            "name": "chunkHash",
            "type": "bytes32"
          }
        ],
        "internalType": "struct ServiceAgreementStructsV1.ProofInputArgs",
        "name": "args",
        "type": "tuple"
      }
    ],
    "name": "sendProof",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "serviceAgreementStorageProxy",
    "outputs": [
      {
        "internalType": "contract ServiceAgreementStorageProxy",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "bool",
        "name": "_status",
        "type": "bool"
      }
    ],
    "name": "setStatus",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "status",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "components": [
          {
            "internalType": "address",
            "name": "assetContract",
            "type": "address"
          },
          {
            "internalType": "uint256",
            "name": "tokenId",
            "type": "uint256"
          },
          {
            "internalType": "bytes",
            "name": "keyword",
            "type": "bytes"
          },
          {
            "internalType": "uint8",
            "name": "hashFunctionId",
            "type": "uint8"
          },
          {
            "internalType": "uint16",
            "name": "epoch",
            "type": "uint16"
          }
        ],
        "internalType": "struct ServiceAgreementStructsV1.CommitInputArgs",
        "name": "args",
        "type": "tuple"
      }
    ],
    "name": "submitCommit",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "assetOwner",
        "type": "address"
      },
      {
        "internalType": "bytes32",
        "name": "agreementId",
        "type": "bytes32"
      }
    ],
    "name": "terminateAgreement",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "tokenContract",
    "outputs": [
      {
        "internalType": "contract IERC20",
        "name": "",
        "type": "address"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "version",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "pure",
    "type": "function"
  }
]
