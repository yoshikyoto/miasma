import React, {Component} from 'react'

/** チャンピオン一覧の中の一つのチャンピオンを表す */
export default class Champion extends Component {
    render() {
        return (<div>{this.props.champion.name}</div>)
    }
}
