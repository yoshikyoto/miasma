import React, {PropTypes, Component} from 'react'
import {AppBar} from 'material-ui'
import FlatButton from 'material-ui/FlatButton';


export default class Header extends Component {
    static get childContextTypes() {
        return { muiTheme: React.PropTypes.object }
    }

    render() {
        return (
            <header className="header">
            <AppBar
            title="LoLProBuild"
            iconElementRight={<FlatButton label="チャンピオン一覧" />} />
            </header>
        )
    }
}
