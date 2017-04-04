import React, {Component} from 'react'
import {connect} from 'react-redux'
import {GridList, GridTile} from 'material-ui/GridList';
import Axios from 'axios'
import {renderChampions} from './reducer.js'
import Champion from './champion.js'

/** チャンピオン一覧 */
class Champions extends Component {


    render() {
        return (
            <div onload={this.getChampions()}>
            <GridList
            cellHeight={120}
            cols={6}
            padding={10}
            style={{
                width: 770, // 120 * 6 + 10 * 5 = 720 + 50
                marginLeft: 'auto',
                marginRight: 'auto',
            }}>
            {this.props.champions.map((champion) => {
                return (
                    <GridTile
                    key={champion.key}
                    title={champion.name}>
                    <img src={champion.icon_url} />
                    </GridTile>
                )
            })}
            </GridList>
            </div>
        )
    }

    /** チャンピオン一覧をまだ取得してなかったら取得して表示 */
    getChampions() {
        if(this.props.champions.length <= 1) {
            Axios.get('/api/v1/champions.json').then(response => {
                this.props.renderChampions(response.data.data);
            });
        }
    }
}

function mapStateToProps(state) {
    return {
        champions: state.championsReducer.champions
    }
}

function mapDispatchToProps(dispatch) {
    return {
        renderChampions: (champions) => {
            dispatch(renderChampions(champions))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Champions)
