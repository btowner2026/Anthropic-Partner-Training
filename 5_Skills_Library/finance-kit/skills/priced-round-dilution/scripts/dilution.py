"""Simple priced equity round only: no convertibles, pool changes or secondary."""
import json,sys

def calculate(p):
    for k in ['pre_money','new_cash','pre_round_shares']:
        if k not in p or not isinstance(p[k],(float,int)) or p[k]<=0: raise ValueError(k+' must be a positive number')
    for k in ['convertibles','pool_top_up','warrants','secondary','fees']:
        if p.get(k): raise ValueError('Unsupported instrument: '+k+'. Build a term-specific model.')
    pre=p['pre_money'];cash=p['new_cash'];shares=p['pre_round_shares'];price=pre/shares;new=cash/price
    return dict(pre_money=pre,new_cash=cash,post_money=pre+cash,price_per_share=price,pre_round_shares=shares,new_shares=new,post_round_shares=shares+new,new_investor_ownership=cash/(pre+cash),existing_holder_ownership=pre/(pre+cash))
if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit('Usage: python dilution.py inputs.json')
    with open(sys.argv[1]) as f: result=calculate(json.load(f))
    print(json.dumps(result,indent=2))
