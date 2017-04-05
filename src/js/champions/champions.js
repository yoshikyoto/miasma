import React, {Component} from 'react'
import {connect} from 'react-redux'
import {GridList, GridTile} from 'material-ui/GridList'
import Subheader from 'material-ui/Subheader'
import TextField from 'material-ui/TextField'
import {Toolbar, ToolbarGroup, ToolbarTitle} from 'material-ui/Toolbar'
import Axios from 'axios'
import {renderAllChampions, renderPartialChampions, searchChampions} from './reducer.js'

/** チャンピオン一覧 */
class Champions extends Component {

    render() {
        return (
            <div onload={this.getChampions()}>
            
            <Toolbar>
            <ToolbarTitle text="チャンピオン一覧" />
            <ToolbarGroup firstChild={true}>
            <TextField
            hintText="チャンピオンを検索"
            onChange={this.props.searchChampions}/>
            </ToolbarGroup>
            </Toolbar>
            
            <GridList
            cellHeight={120}
            cols={6}
            padding={10}
            style={{
                width: 790, // 120 * 6 + 10 * 7 = 720 + 70
                marginLeft: 'auto',
                marginRight: 'auto',
            }}>
            
            {this.props.champions.map((champion) => {
                return (
                    <GridTile
                    key={champion.key}
                    title={champion.name}
                    titleStyle={{
                        fontSize: 12,
                    }}>
                    <img src={champion.icon_url} />
                    </GridTile>
                )
            })}
            
            </GridList>
            </div>
        )
    }

    /** チャンピオン一覧をまだ取得してなかったら取得してpropertyにset */
    getChampions() {
        if(this.props.allChampions.length <= 1) {
            Axios.get('/api/v1/champions.json').then(response => {
                this.props.renderAllChampions(response.data.data)
            });
        }
    }
}

function mapStateToProps(state) {
    return {
        allChampions: state.championsReducer.allChampions,
        champions: state.championsReducer.champions,
    }
}

function mapDispatchToProps(dispatch) {
    return {
        renderAllChampions: (champions) => {
            dispatch(renderAllChampions(champions))
        },
        searchChampions: (event, newValue) => {
            dispatch(searchChampions(newValue))
        },
        renderPartialChampions: (champions) => {
            dispatch(renderPartialChampions(champions))
        }
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Champions)
