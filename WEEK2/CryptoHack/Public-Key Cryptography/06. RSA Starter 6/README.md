# RSA Starter 6

## Description

How can you ensure that the person receiving your message knows that you wrote it?

You've been asked out on a date, and you want to send a message telling them that you'd love to go, however a jealous lover isn't so happy about this.  

When you send your message saying yes, your jealous lover intercepts the message and corrupts it so it now says no!  

We can protect against these attacks by signing the message.  

Imagine you write a message `M`. You encrypt this message with your **friend's public key**: $C = M^{e_0}\ mod\ N_0$.  

To sign this message, you calculate the hash of the message: `H(M)` and "encrypt" this with **your private key**: $S = [H(M)]^{d_1}\ mod\ N_1$.  

> In real cryptosystems, it's [best practice to use separate keys](https://crypto.stackexchange.com/a/12138) for encrypting and signing messages.  

Your friend can decrypt the message using **their private key**: $m = C^{d_0}\ mod\ N_0$. Using your public key they calculate $s = S^{e_1}\ mod\ N_1$.  

Now by computing `H(m)` and comparing it to `s`: `assert H(m) == s`, they can ensure that the message you sent them, is the message that they received!  

Sign the flag `crypto{Immut4ble_m3ssag1ng}` using your private key and the SHA256 hash function.  

> The output of the hash function needs to be converted into a number that can be used with RSA math. Remember the helpful `bytes_to_long()` function that can be imported from `Crypto.Util.number`.  

**Challenge files:**  

- [private.key](./private.key)

## Solution

We are given a file [`private.key`](./private.key) containing private key values `N` and `d`. Given flag `crypto{Immut4ble_m3ssag1ng}`, we are to sign the flag using the given private key and SHA256 hashing function. Let flag be `m`, I calculate `H(m)` which is the hashed message in integer form and then signature is calculated by $s = [H(m)]^d\ mod\ N$.

Complete solution is given in [`solve.py`](./solve.py).

```bash
$ python3 solve.py
signature = 13480738404590090803339831649238454376183189744970683129909766078877706583282422686710545217275797376709672358894231550335007974983458408620258478729775647818876610072903021235573923300070103666940534047644900475773318682585772698155617451477448441198150710420818995347235921111812068656782998168064960965451719491072569057636701190429760047193261886092862024118487826452766513533860734724124228305158914225250488399673645732882077575252662461860972889771112594906884441454355959482925283992539925713424132009768721389828848907099772040836383856524605008942907083490383109757406940540866978237471686296661685839083475
```

## Answer

`13480738404590090803339831649238454376183189744970683129909766078877706583282422686710545217275797376709672358894231550335007974983458408620258478729775647818876610072903021235573923300070103666940534047644900475773318682585772698155617451477448441198150710420818995347235921111812068656782998168064960965451719491072569057636701190429760047193261886092862024118487826452766513533860734724124228305158914225250488399673645732882077575252662461860972889771112594906884441454355959482925283992539925713424132009768721389828848907099772040836383856524605008942907083490383109757406940540866978237471686296661685839083475`
