import pandas as pd


data = pd.DataFrame({
    'Player': ['Player1', 'Player2', 'Player3', 'Player4'],
    'Match': ['Match1', 'Match1', 'Match1', 'Match1'],
    'Catches': [2, 1, 0, 3],
    'RunOuts': [1, 0, 2, 1],
    'Stops': [5, 3, 4, 2],
    'Misfields': [0, 1, 0, 2],
    'DirectHits': [1, 0, 1, 0],
    'DroppedCatches': [0, 1, 0, 0]
})


players = ['Player1', 'Player2', 'Player3']


fielding_data = data[data['Player'].isin(players)]


fielding_data['EffectiveFielding'] = (
    fielding_data['Catches'] * 10 + 
    fielding_data['RunOuts'] * 12 + 
    fielding_data['DirectHits'] * 8 + 
    fielding_data['Stops'] * 2
)
fielding_data['Errors'] = (
    fielding_data['Misfields'] * 5 + 
    fielding_data['DroppedCatches'] * 7
)


fielding_data['NetFieldingScore'] = fielding_data['EffectiveFielding'] - fielding_data['Errors']

summary = fielding_data[['Player', 'EffectiveFielding', 'Errors', 'NetFieldingScore']]


print(summary)
