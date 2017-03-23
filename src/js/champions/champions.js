import React, {Component} from 'react'
import {connect} from 'react-redux'
import {bindActionCreators} from 'redux'
import Axios from 'axios'
import {renderChampions} from './reducer.js'
import Champion from './champion.js'

/** チャンピオン一覧 */
class Champions extends Component {
    render() {
        return (
                <div onLoad={this.getChampions()}>
                {this.props.champions.map((champion) => {
                    return <Champion champion={champion}/>
                })}
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
