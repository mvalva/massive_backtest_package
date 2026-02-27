from pathlib import Path
import pandas as pd
import sys

sys.path.insert(0, str(Path('.').resolve()))
sys.path.insert(0, str(Path('massive_backtest').resolve()))

# Force reload
if 'massive_backtest.strategy_agent' in sys.modules:
    del sys.modules['massive_backtest.strategy_agent']

from massive_backtest.strategy_agent import (
    build_10k_strategy,
    STRATEGY_10K_BUDGET,
    STRATEGY_10K_LOOKBACK_DAYS,
    STRATEGY_10K_MAX_POSITIONS,
)

df = pd.read_csv('STRATEGY_AGENT_CASES.csv', sep=';', encoding='utf-8-sig', low_memory=False)
rank = pd.read_csv('STRATEGY_AGENT_RANKING.csv', sep=';', encoding='utf-8-sig').to_dict('records')

build_10k_strategy(
    df, rank,
    out_path=Path('STRATEGY_AGENT_10K.md'),
    out_path_csv=Path('STRATEGY_AGENT_10K.csv'),
    budget_usd=STRATEGY_10K_BUDGET,
    lookback_days=STRATEGY_10K_LOOKBACK_DAYS,
    max_positions=STRATEGY_10K_MAX_POSITIONS,
    top_strategies_k=10,
)

print('OK')
