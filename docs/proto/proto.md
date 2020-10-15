# Protocol Documentation
<a name="top"/>

## Table of Contents

- [dc.proto](#dc.proto)
    - [AddressList](#dc.AddressList)
    - [AddressState](#dc.AddressState)
    - [Block](#dc.Block)
    - [BlockExtended](#dc.BlockExtended)
    - [BlockHeader](#dc.BlockHeader)
    - [BlockHeaderExtended](#dc.BlockHeaderExtended)
    - [BlockMetaData](#dc.BlockMetaData)
    - [BlockMetaDataList](#dc.BlockMetaDataList)
    - [EphemeralMessage](#dc.EphemeralMessage)
    - [GenesisBalance](#dc.GenesisBalance)
    - [GetAddressStateReq](#dc.GetAddressStateReq)
    - [GetAddressStateResp](#dc.GetAddressStateResp)
    - [GetBlockReq](#dc.GetBlockReq)
    - [GetBlockResp](#dc.GetBlockResp)
    - [GetKnownPeersReq](#dc.GetKnownPeersReq)
    - [GetKnownPeersResp](#dc.GetKnownPeersResp)
    - [GetLatestDataReq](#dc.GetLatestDataReq)
    - [GetLatestDataResp](#dc.GetLatestDataResp)
    - [GetLocalAddressesReq](#dc.GetLocalAddressesReq)
    - [GetLocalAddressesResp](#dc.GetLocalAddressesResp)
    - [GetNodeStateReq](#dc.GetNodeStateReq)
    - [GetNodeStateResp](#dc.GetNodeStateResp)
    - [GetObjectReq](#dc.GetObjectReq)
    - [GetObjectResp](#dc.GetObjectResp)
    - [GetStakersReq](#dc.GetStakersReq)
    - [GetStakersResp](#dc.GetStakersResp)
    - [GetStatsReq](#dc.GetStatsReq)
    - [GetStatsResp](#dc.GetStatsResp)
    - [GetWalletReq](#dc.GetWalletReq)
    - [GetWalletResp](#dc.GetWalletResp)
    - [LatticePublicKeyTxnReq](#dc.LatticePublicKeyTxnReq)
    - [MR](#dc.MR)
    - [MsgObject](#dc.MsgObject)
    - [NodeInfo](#dc.NodeInfo)
    - [Peer](#dc.Peer)
    - [PingReq](#dc.PingReq)
    - [PongResp](#dc.PongResp)
    - [PushTransactionReq](#dc.PushTransactionReq)
    - [PushTransactionResp](#dc.PushTransactionResp)
    - [StakeValidator](#dc.StakeValidator)
    - [StakeValidatorsList](#dc.StakeValidatorsList)
    - [StakeValidatorsTracker](#dc.StakeValidatorsTracker)
    - [StakeValidatorsTracker.ExpiryEntry](#dc.StakeValidatorsTracker.ExpiryEntry)
    - [StakeValidatorsTracker.FutureStakeAddressesEntry](#dc.StakeValidatorsTracker.FutureStakeAddressesEntry)
    - [StakeValidatorsTracker.FutureSvDictEntry](#dc.StakeValidatorsTracker.FutureSvDictEntry)
    - [StakeValidatorsTracker.SvDictEntry](#dc.StakeValidatorsTracker.SvDictEntry)
    - [StakerData](#dc.StakerData)
    - [StoredPeers](#dc.StoredPeers)
    - [Timestamp](#dc.Timestamp)
    - [Transaction](#dc.Transaction)
    - [Transaction.CoinBase](#dc.Transaction.CoinBase)
    - [Transaction.Destake](#dc.Transaction.Destake)
    - [Transaction.Duplicate](#dc.Transaction.Duplicate)
    - [Transaction.LatticePublicKey](#dc.Transaction.LatticePublicKey)
    - [Transaction.Stake](#dc.Transaction.Stake)
    - [Transaction.Transfer](#dc.Transaction.Transfer)
    - [Transaction.Vote](#dc.Transaction.Vote)
    - [TransactionCount](#dc.TransactionCount)
    - [TransactionCount.CountEntry](#dc.TransactionCount.CountEntry)
    - [TransactionExtended](#dc.TransactionExtended)
    - [TransferCoinsReq](#dc.TransferCoinsReq)
    - [TransferCoinsResp](#dc.TransferCoinsResp)
    - [Wallet](#dc.Wallet)
    - [WalletStore](#dc.WalletStore)

    - [GetLatestDataReq.Filter](#dc.GetLatestDataReq.Filter)
    - [GetStakersReq.Filter](#dc.GetStakersReq.Filter)
    - [NodeInfo.State](#dc.NodeInfo.State)
    - [Transaction.Type](#dc.Transaction.Type)


    - [AdminAPI](#dc.AdminAPI)
    - [P2PAPI](#dc.P2PAPI)
    - [PublicAPI](#dc.PublicAPI)


- [dcbase.proto](#dcbase.proto)
    - [GetNodeInfoReq](#dc.GetNodeInfoReq)
    - [GetNodeInfoResp](#dc.GetNodeInfoResp)



    - [Base](#dc.Base)


- [dclegacy.proto](#dclegacy.proto)
    - [BKData](#dc.BKData)
    - [FBData](#dc.FBData)
    - [LegacyMessage](#dc.LegacyMessage)
    - [MRData](#dc.MRData)
    - [NoData](#dc.NoData)
    - [PBData](#dc.PBData)
    - [PLData](#dc.PLData)
    - [PONGData](#dc.PONGData)
    - [SYNCData](#dc.SYNCData)
    - [VEData](#dc.VEData)

    - [LegacyMessage.FuncName](#dc.LegacyMessage.FuncName)




- [Scalar Value Types](#scalar-value-types)



<a name="dc.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dc.proto



<a name="dc.AddressList"/>

### AddressList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="dc.AddressState"/>

### AddressState



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  | FIXME: Discuss. 32 or 64 bits? |
| pubhashes | [bytes](#bytes) | repeated |  |
| transaction_hashes | [bytes](#bytes) | repeated |  |






<a name="dc.Block"/>

### Block



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#dc.BlockHeader) |  |  |
| transactions | [Transaction](#dc.Transaction) | repeated |  |
| dup_transactions | [Transaction](#dc.Transaction) | repeated | TODO: Review this |
| vote | [Transaction](#dc.Transaction) | repeated |  |
| genesis_balance | [GenesisBalance](#dc.GenesisBalance) | repeated | This is only applicable to genesis blocks |






<a name="dc.BlockExtended"/>

### BlockExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block | [Block](#dc.Block) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="dc.BlockHeader"/>

### BlockHeader



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  | Header |
| epoch | [uint64](#uint64) |  |  |
| timestamp | [Timestamp](#dc.Timestamp) |  | FIXME: Temporary |
| hash_header | [bytes](#bytes) |  |  |
| hash_header_prev | [bytes](#bytes) |  |  |
| reward_block | [uint64](#uint64) |  |  |
| reward_fee | [uint64](#uint64) |  |  |
| merkle_root | [bytes](#bytes) |  |  |
| hash_reveal | [bytes](#bytes) |  |  |
| stake_selector | [bytes](#bytes) |  |  |






<a name="dc.BlockHeaderExtended"/>

### BlockHeaderExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#dc.BlockHeader) |  |  |
| transaction_count | [TransactionCount](#dc.TransactionCount) |  |  |
| voted_weight | [uint64](#uint64) |  |  |
| total_stake_weight | [uint64](#uint64) |  |  |






<a name="dc.BlockMetaData"/>

### BlockMetaData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="dc.BlockMetaDataList"/>

### BlockMetaDataList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number_hashes | [BlockMetaData](#dc.BlockMetaData) | repeated |  |






<a name="dc.EphemeralMessage"/>

### EphemeralMessage



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| id | [bytes](#bytes) |  |  |
| ttl | [uint64](#uint64) |  |  |
| data | [bytes](#bytes) |  | Encrypted String containing aes256_symkey, prf512_seed, xmss_address, signature |






<a name="dc.EphemeralMessage.Data"/>

### EphemeralMessage.Data



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| aes256_symkey | [bytes](#bytes) |  |  |
| prf512_seed | [bytes](#bytes) |  |  |
| xmss_address | [bytes](#bytes) |  |  |
| xmss_signature | [bytes](#bytes) |  |  |






<a name="dc.GenesisBalance"/>

### GenesisBalance



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | Address is string only here to increase visibility |
| balance | [uint64](#uint64) |  |  |






<a name="dc.GetAddressStateReq"/>

### GetAddressStateReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="dc.GetAddressStateResp"/>

### GetAddressStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| state | [AddressState](#dc.AddressState) |  |  |






<a name="dc.GetBlockReq"/>

### GetBlockReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  | Indicates the index number in mainchain |
| after_hash | [bytes](#bytes) |  | request the node that comes after hash |






<a name="dc.GetBlockResp"/>

### GetBlockResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#dc.NodeInfo) |  |  |
| block | [Block](#dc.Block) |  |  |






<a name="dc.GetKnownPeersReq"/>

### GetKnownPeersReq







<a name="dc.GetKnownPeersResp"/>

### GetKnownPeersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#dc.NodeInfo) |  |  |
| known_peers | [Peer](#dc.Peer) | repeated |  |






<a name="dc.GetLatestDataReq"/>

### GetLatestDataReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetLatestDataReq.Filter](#dc.GetLatestDataReq.Filter) |  |  |
| offset | [uint32](#uint32) |  | Offset in the result list (works backwards in this case) |
| quantity | [uint32](#uint32) |  | Number of items to retrive. Capped at 100 |






<a name="dc.GetLatestDataResp"/>

### GetLatestDataResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| blockheaders | [BlockHeaderExtended](#dc.BlockHeaderExtended) | repeated |  |
| transactions | [TransactionExtended](#dc.TransactionExtended) | repeated |  |
| transactions_unconfirmed | [TransactionExtended](#dc.TransactionExtended) | repeated |  |






<a name="dc.GetLocalAddressesReq"/>

### GetLocalAddressesReq







<a name="dc.GetLocalAddressesResp"/>

### GetLocalAddressesResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addresses | [bytes](#bytes) | repeated |  |






<a name="dc.GetNodeStateReq"/>

### GetNodeStateReq







<a name="dc.GetNodeStateResp"/>

### GetNodeStateResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| info | [NodeInfo](#dc.NodeInfo) |  |  |






<a name="dc.GetObjectReq"/>

### GetObjectReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| query | [bytes](#bytes) |  |  |






<a name="dc.GetObjectResp"/>

### GetObjectResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| found | [bool](#bool) |  |  |
| address_state | [AddressState](#dc.AddressState) |  |  |
| transaction | [TransactionExtended](#dc.TransactionExtended) |  |  |
| block | [Block](#dc.Block) |  |  |






<a name="dc.GetStakersReq"/>

### GetStakersReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| filter | [GetStakersReq.Filter](#dc.GetStakersReq.Filter) |  | Indicates which group of stakers (current / next) |
| offset | [uint32](#uint32) |  | Offset in the staker list |
| quantity | [uint32](#uint32) |  | Number of stakers to retrive. Capped at 100 |






<a name="dc.GetStakersResp"/>

### GetStakersResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stakers | [StakerData](#dc.StakerData) | repeated |  |






<a name="dc.GetStatsReq"/>

### GetStatsReq







<a name="dc.GetStatsResp"/>

### GetStatsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| node_info | [NodeInfo](#dc.NodeInfo) |  |  |
| epoch | [uint64](#uint64) |  | Current epoch |
| uptime_network | [uint64](#uint64) |  | Indicates uptime in seconds |
| stakers_count | [uint64](#uint64) |  | Number of active stakers |
| block_last_reward | [uint64](#uint64) |  |  |
| block_time_mean | [uint64](#uint64) |  |  |
| block_time_sd | [uint64](#uint64) |  |  |
| coins_total_supply | [uint64](#uint64) |  |  |
| coins_emitted | [uint64](#uint64) |  |  |
| coins_atstake | [uint64](#uint64) |  |  |






<a name="dc.GetWalletReq"/>

### GetWalletReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |






<a name="dc.GetWalletResp"/>

### GetWalletResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallet | [Wallet](#dc.Wallet) |  | FIXME: Encrypt |






<a name="dc.LatticePublicKeyTxnReq"/>

### LatticePublicKeyTxnReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  |  |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |
| xmss_pk | [bytes](#bytes) |  |  |
| xmss_ots_index | [uint64](#uint64) |  |  |






<a name="dc.MR"/>

### MR
FIXME: This is legacy. Plan removal


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [string](#string) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="dc.MsgObject"/>

### MsgObject



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ephemeral | [EphemeralMessage](#dc.EphemeralMessage) |  | Overlapping - objects used for 2-way exchanges P2PRequest request = 1; P2PResponse response = 2; |






<a name="dc.NodeInfo"/>

### NodeInfo



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| state | [NodeInfo.State](#dc.NodeInfo.State) |  |  |
| num_connections | [uint32](#uint32) |  |  |
| num_known_peers | [uint32](#uint32) |  |  |
| uptime | [uint64](#uint64) |  | Uptime in seconds |
| block_height | [uint64](#uint64) |  |  |
| block_last_hash | [bytes](#bytes) |  |  |
| stake_enabled | [bool](#bool) |  |  |
| network_id | [string](#string) |  |  |






<a name="dc.Peer"/>

### Peer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ip | [string](#string) |  |  |






<a name="dc.PingReq"/>

### PingReq







<a name="dc.PongResp"/>

### PongResp







<a name="dc.PushTransactionReq"/>

### PushTransactionReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_signed | [Transaction](#dc.Transaction) |  |  |






<a name="dc.PushTransactionResp"/>

### PushTransactionResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| some_response | [string](#string) |  |  |






<a name="dc.StakeValidator"/>

### StakeValidator



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [bytes](#bytes) |  |  |
| slave_public_key | [bytes](#bytes) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |
| balance | [uint64](#uint64) |  |  |
| activation_blocknumber | [uint64](#uint64) |  |  |
| nonce | [uint64](#uint64) |  |  |
| is_banned | [bool](#bool) |  |  |
| is_active | [bool](#bool) |  |  |






<a name="dc.StakeValidatorsList"/>

### StakeValidatorsList



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| stake_validators | [StakeValidator](#dc.StakeValidator) | repeated |  |






<a name="dc.StakeValidatorsTracker"/>

### StakeValidatorsTracker



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| sv_dict | [StakeValidatorsTracker.SvDictEntry](#dc.StakeValidatorsTracker.SvDictEntry) | repeated |  |
| future_stake_addresses | [StakeValidatorsTracker.FutureStakeAddressesEntry](#dc.StakeValidatorsTracker.FutureStakeAddressesEntry) | repeated |  |
| expiry | [StakeValidatorsTracker.ExpiryEntry](#dc.StakeValidatorsTracker.ExpiryEntry) | repeated |  |
| future_sv_dict | [StakeValidatorsTracker.FutureSvDictEntry](#dc.StakeValidatorsTracker.FutureSvDictEntry) | repeated |  |
| total_stake_amount | [uint64](#uint64) |  |  |






<a name="dc.StakeValidatorsTracker.ExpiryEntry"/>

### StakeValidatorsTracker.ExpiryEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [AddressList](#dc.AddressList) |  |  |






<a name="dc.StakeValidatorsTracker.FutureStakeAddressesEntry"/>

### StakeValidatorsTracker.FutureStakeAddressesEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#dc.StakeValidator) |  |  |






<a name="dc.StakeValidatorsTracker.FutureSvDictEntry"/>

### StakeValidatorsTracker.FutureSvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint64](#uint64) |  |  |
| value | [StakeValidatorsList](#dc.StakeValidatorsList) |  |  |






<a name="dc.StakeValidatorsTracker.SvDictEntry"/>

### StakeValidatorsTracker.SvDictEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [string](#string) |  |  |
| value | [StakeValidator](#dc.StakeValidator) |  |  |






<a name="dc.StakerData"/>

### StakerData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_state | [AddressState](#dc.AddressState) |  |  |
| terminator_hash | [bytes](#bytes) |  |  |






<a name="dc.StoredPeers"/>

### StoredPeers



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peers | [Peer](#dc.Peer) | repeated |  |






<a name="dc.Timestamp"/>

### Timestamp
TODO: Avoid using timestamp until the github issue is fixed
import &#34;google/protobuf/timestamp.proto&#34;;


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| seconds | [int64](#int64) |  |  |
| nanos | [int32](#int32) |  |  |






<a name="dc.Transaction"/>

### Transaction



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| type | [Transaction.Type](#dc.Transaction.Type) |  |  |
| nonce | [uint64](#uint64) |  |  |
| addr_from | [bytes](#bytes) |  |  |
| public_key | [bytes](#bytes) |  |  |
| transaction_hash | [bytes](#bytes) |  |  |
| ots_key | [uint32](#uint32) |  |  |
| signature | [bytes](#bytes) |  |  |
| transfer | [Transaction.Transfer](#dc.Transaction.Transfer) |  |  |
| stake | [Transaction.Stake](#dc.Transaction.Stake) |  |  |
| coinbase | [Transaction.CoinBase](#dc.Transaction.CoinBase) |  |  |
| latticePK | [Transaction.LatticePublicKey](#dc.Transaction.LatticePublicKey) |  |  |
| duplicate | [Transaction.Duplicate](#dc.Transaction.Duplicate) |  |  |
| vote | [Transaction.Vote](#dc.Transaction.Vote) |  |  |






<a name="dc.Transaction.CoinBase"/>

### Transaction.CoinBase



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |






<a name="dc.Transaction.Destake"/>

### Transaction.Destake







<a name="dc.Transaction.Duplicate"/>

### Transaction.Duplicate



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| prev_header_hash | [uint64](#uint64) |  |  |
| coinbase1_hhash | [bytes](#bytes) |  |  |
| coinbase2_hhash | [bytes](#bytes) |  |  |
| coinbase1 | [Transaction](#dc.Transaction) |  |  |
| coinbase2 | [Transaction](#dc.Transaction) |  |  |






<a name="dc.Transaction.LatticePublicKey"/>

### Transaction.LatticePublicKey



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| kyber_pk | [bytes](#bytes) |  |  |
| dilithium_pk | [bytes](#bytes) |  |  |






<a name="dc.Transaction.Stake"/>

### Transaction.Stake



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| activation_blocknumber | [uint64](#uint64) |  |  |
| slavePK | [bytes](#bytes) |  |  |
| hash | [bytes](#bytes) |  |  |






<a name="dc.Transaction.Transfer"/>

### Transaction.Transfer



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| addr_to | [bytes](#bytes) |  |  |
| amount | [uint64](#uint64) |  |  |
| fee | [uint64](#uint64) |  |  |






<a name="dc.Transaction.Vote"/>

### Transaction.Vote



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| block_number | [uint64](#uint64) |  |  |
| hash_header | [bytes](#bytes) |  |  |






<a name="dc.TransactionCount"/>

### TransactionCount



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| count | [TransactionCount.CountEntry](#dc.TransactionCount.CountEntry) | repeated |  |






<a name="dc.TransactionCount.CountEntry"/>

### TransactionCount.CountEntry



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| key | [uint32](#uint32) |  |  |
| value | [uint32](#uint32) |  |  |






<a name="dc.TransactionExtended"/>

### TransactionExtended



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| header | [BlockHeader](#dc.BlockHeader) |  |  |
| tx | [Transaction](#dc.Transaction) |  |  |






<a name="dc.TransferCoinsReq"/>

### TransferCoinsReq



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address_from | [bytes](#bytes) |  | Transaction source address |
| address_to | [bytes](#bytes) |  | Transaction destination address |
| amount | [uint64](#uint64) |  | Amount. It should be expressed in Shor |
| fee | [uint64](#uint64) |  | Fee. It should be expressed in Shor |
| xmss_pk | [bytes](#bytes) |  | XMSS Public key |
| xmss_ots_index | [uint64](#uint64) |  | XMSS One time signature index |






<a name="dc.TransferCoinsResp"/>

### TransferCoinsResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| transaction_unsigned | [Transaction](#dc.Transaction) |  |  |






<a name="dc.Wallet"/>

### Wallet



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| address | [string](#string) |  | FIXME move to bytes |
| mnemonic | [string](#string) |  |  |
| xmss_index | [int32](#int32) |  |  |






<a name="dc.WalletStore"/>

### WalletStore



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| wallets | [Wallet](#dc.Wallet) | repeated |  |








<a name="dc.GetLatestDataReq.Filter"/>

### GetLatestDataReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| ALL | 0 |  |
| BLOCKHEADERS | 1 |  |
| TRANSACTIONS | 2 |  |
| TRANSACTIONS_UNCONFIRMED | 3 |  |



<a name="dc.GetStakersReq.Filter"/>

### GetStakersReq.Filter


| Name | Number | Description |
| ---- | ------ | ----------- |
| CURRENT | 0 |  |
| NEXT | 1 |  |



<a name="dc.NodeInfo.State"/>

### NodeInfo.State


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| UNSYNCED | 1 |  |
| SYNCING | 2 |  |
| SYNCED | 3 |  |
| FORKED | 4 |  |



<a name="dc.Transaction.Type"/>

### Transaction.Type


| Name | Number | Description |
| ---- | ------ | ----------- |
| UNKNOWN | 0 |  |
| TRANSFER | 1 |  |
| STAKE | 2 |  |
| DESTAKE | 3 |  |
| COINBASE | 4 |  |
| LATTICE | 5 |  |
| DUPLICATE | 6 |  |
| VOTE | 7 |  |







<a name="dc.AdminAPI"/>

### AdminAPI
This is a place holder for testing/instrumentation APIs

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLocalAddresses | [GetLocalAddressesReq](#dc.GetLocalAddressesReq) | [GetLocalAddressesResp](#dc.GetLocalAddressesReq) | FIXME: Use TLS and some signature scheme to validate the cli? At the moment, it will run locally |


<a name="dc.P2PAPI"/>

### P2PAPI
This service describes the P2P API

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#dc.GetNodeStateReq) | [GetNodeStateResp](#dc.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#dc.GetKnownPeersReq) | [GetKnownPeersResp](#dc.GetKnownPeersReq) |  |
| GetBlock | [GetBlockReq](#dc.GetBlockReq) | [GetBlockResp](#dc.GetBlockReq) | rpc PublishBlock(PublishBlockReq) returns (PublishBlockResp); |
| ObjectExchange | [MsgObject](#dc.MsgObject) | [MsgObject](#dc.MsgObject) | A bidirectional streaming channel is used to avoid any firewalling/NAT issues. |


<a name="dc.PublicAPI"/>

### PublicAPI
This service describes the Public API used by clients (wallet/cli/etc)

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeState | [GetNodeStateReq](#dc.GetNodeStateReq) | [GetNodeStateResp](#dc.GetNodeStateReq) |  |
| GetKnownPeers | [GetKnownPeersReq](#dc.GetKnownPeersReq) | [GetKnownPeersResp](#dc.GetKnownPeersReq) |  |
| GetStats | [GetStatsReq](#dc.GetStatsReq) | [GetStatsResp](#dc.GetStatsReq) |  |
| GetAddressState | [GetAddressStateReq](#dc.GetAddressStateReq) | [GetAddressStateResp](#dc.GetAddressStateReq) |  |
| GetObject | [GetObjectReq](#dc.GetObjectReq) | [GetObjectResp](#dc.GetObjectReq) |  |
| GetLatestData | [GetLatestDataReq](#dc.GetLatestDataReq) | [GetLatestDataResp](#dc.GetLatestDataReq) |  |
| GetStakers | [GetStakersReq](#dc.GetStakersReq) | [GetStakersResp](#dc.GetStakersReq) |  |
| TransferCoins | [TransferCoinsReq](#dc.TransferCoinsReq) | [TransferCoinsResp](#dc.TransferCoinsReq) |  |
| PushTransaction | [PushTransactionReq](#dc.PushTransactionReq) | [PushTransactionResp](#dc.PushTransactionReq) |  |
| GetLatticePublicKeyTxn | [LatticePublicKeyTxnReq](#dc.LatticePublicKeyTxnReq) | [TransferCoinsResp](#dc.LatticePublicKeyTxnReq) |  |





<a name="dcbase.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dcbase.proto



<a name="dc.GetNodeInfoReq"/>

### GetNodeInfoReq







<a name="dc.GetNodeInfoResp"/>

### GetNodeInfoResp



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| grpcProto | [string](#string) |  |  |












<a name="dc.Base"/>

### Base


| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetNodeInfo | [GetNodeInfoReq](#dc.GetNodeInfoReq) | [GetNodeInfoResp](#dc.GetNodeInfoReq) |  |





<a name="dclegacy.proto"/>
<p align="right"><a href="#top">Top</a></p>

## dclegacy.proto



<a name="dc.BKData"/>

### BKData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mrData | [MRData](#dc.MRData) |  |  |
| block | [Block](#dc.Block) |  |  |






<a name="dc.FBData"/>

### FBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |






<a name="dc.LegacyMessage"/>

### LegacyMessage
Adding old code to refactor while keeping things working


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| func_name | [LegacyMessage.FuncName](#dc.LegacyMessage.FuncName) |  |  |
| noData | [NoData](#dc.NoData) |  |  |
| veData | [VEData](#dc.VEData) |  |  |
| pongData | [PONGData](#dc.PONGData) |  |  |
| mrData | [MRData](#dc.MRData) |  |  |
| sfmData | [MRData](#dc.MRData) |  |  |
| bkData | [BKData](#dc.BKData) |  |  |
| fbData | [FBData](#dc.FBData) |  |  |
| pbData | [PBData](#dc.PBData) |  |  |
| pbbData | [PBData](#dc.PBData) |  |  |
| syncData | [SYNCData](#dc.SYNCData) |  |  |






<a name="dc.MRData"/>

### MRData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| hash | [bytes](#bytes) |  | FIXME: rename this to block_headerhash |
| type | [LegacyMessage.FuncName](#dc.LegacyMessage.FuncName) |  | FIXME: type/string what is this |
| stake_selector | [bytes](#bytes) |  |  |
| block_number | [uint64](#uint64) |  |  |
| prev_headerhash | [bytes](#bytes) |  |  |
| reveal_hash | [bytes](#bytes) |  |  |






<a name="dc.NoData"/>

### NoData







<a name="dc.PBData"/>

### PBData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| index | [uint64](#uint64) |  |  |
| block | [Block](#dc.Block) |  |  |






<a name="dc.PLData"/>

### PLData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| peer_ips | [string](#string) | repeated |  |






<a name="dc.PONGData"/>

### PONGData







<a name="dc.SYNCData"/>

### SYNCData







<a name="dc.VEData"/>

### VEData



| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| version | [string](#string) |  |  |
| genesis_prev_hash | [bytes](#bytes) |  |  |








<a name="dc.LegacyMessage.FuncName"/>

### LegacyMessage.FuncName


| Name | Number | Description |
| ---- | ------ | ----------- |
| VE | 0 | Version |
| PL | 1 | Peers List |
| PONG | 2 | Pong |
| MR | 3 | Message received |
| SFM | 4 | Send Full Message |
| BK | 5 | Block |
| FB | 6 | Fetch request for block |
| PB | 7 | Push Block |
| PBB | 8 | Push Block Buffer |
| ST | 9 | Stake Transaction |
| DST | 10 | Destake Transaction |
| DT | 11 | Duplicate Transaction |
| TX | 12 | Transfer Transaction |
| VT | 13 | Vote |
| SYNC | 14 | Add into synced list, if the node replies |










## Scalar Value Types

| .proto Type | Notes | C++ Type | Java Type | Python Type |
| ----------- | ----- | -------- | --------- | ----------- |
| <a name="double" /> double |  | double | double | float |
| <a name="float" /> float |  | float | float | float |
| <a name="int32" /> int32 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint32 instead. | int32 | int | int |
| <a name="int64" /> int64 | Uses variable-length encoding. Inefficient for encoding negative numbers – if your field is likely to have negative values, use sint64 instead. | int64 | long | int/long |
| <a name="uint32" /> uint32 | Uses variable-length encoding. | uint32 | int | int/long |
| <a name="uint64" /> uint64 | Uses variable-length encoding. | uint64 | long | int/long |
| <a name="sint32" /> sint32 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int32s. | int32 | int | int |
| <a name="sint64" /> sint64 | Uses variable-length encoding. Signed int value. These more efficiently encode negative numbers than regular int64s. | int64 | long | int/long |
| <a name="fixed32" /> fixed32 | Always four bytes. More efficient than uint32 if values are often greater than 2^28. | uint32 | int | int |
| <a name="fixed64" /> fixed64 | Always eight bytes. More efficient than uint64 if values are often greater than 2^56. | uint64 | long | int/long |
| <a name="sfixed32" /> sfixed32 | Always four bytes. | int32 | int | int |
| <a name="sfixed64" /> sfixed64 | Always eight bytes. | int64 | long | int/long |
| <a name="bool" /> bool |  | bool | boolean | boolean |
| <a name="string" /> string | A string must always contain UTF-8 encoded or 7-bit ASCII text. | string | String | str/unicode |
| <a name="bytes" /> bytes | May contain any arbitrary sequence of bytes. | string | ByteString | str |

