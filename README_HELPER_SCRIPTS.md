# 🎯 Helper Scripts for Validator 8499 Withdrawal Address Update

This repository fork includes ready-to-use helper scripts for updating the withdrawal address of validator 8499.

## 🚀 Quick Start (Just 3 Steps!)

### Step 1: Install Dependencies
```bash
pip3 install -r requirements.txt
python3 setup.py install
```

### Step 2: Run the Helper Script
```bash
./run_withdrawal_address_update.sh
```

### Step 3: Submit the Generated File
After the script completes, submit the generated file (`bls_to_execution_changes/bls_to_execution_change-*.json`) to the Ethereum network.

---

## 📁 What's Included

This repository contains:

- ✅ **Interactive shell script** - `run_withdrawal_address_update.sh`
- ✅ **Python helper script** - `update_withdrawal_address_example.py`
- ✅ **Quick start guide** - `QUICKSTART.md`
- ✅ **Comprehensive guide** - `WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md`
- ✅ **Summary document** - `SUMMARY.md`

## 📋 Configuration

All helper scripts use these pre-configured parameters:

| Parameter | Value |
|-----------|-------|
| Validator Index | `8499` |
| Old Credentials | `0x00101ca78a5ea9aad05eeffebadc2734754badb9620a4adb366e6013da054b51` |
| New Address | `0x06EE840642a33367ee59fCA237F270d5119d1356` |
| Network | `mainnet` |

## 🔒 Security Warning

**IMPORTANT:** 
- Run on an **OFFLINE** device
- **NEVER** share your mnemonic
- **VERIFY** all parameters before confirming
- This operation is **IRREVERSIBLE**

## 📚 Documentation

Choose your reading level:

1. **Just want to run it?** → Start here: `QUICKSTART.md`
2. **Want detailed instructions?** → Read: `WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md`
3. **Want an overview?** → See: `SUMMARY.md`

## 🆘 Quick Troubleshooting

**"Module not found" error?**
```bash
pip3 install pycryptodome
```

**"Permission denied" error?**
```bash
chmod +x run_withdrawal_address_update.sh
chmod +x deposit.sh
```

**Need more help?**
Check `WITHDRAWAL_ADDRESS_UPDATE_GUIDE.md` for detailed troubleshooting.

## 📞 Support

- Issues: https://github.com/ethereum/staking-deposit-cli/issues
- Validator Status: https://beaconcha.in/validator/8499

---

**Good luck with your withdrawal address update!** 🎉
