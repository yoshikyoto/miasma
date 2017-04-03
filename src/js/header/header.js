import React, {PropTypes, Component} from 'react'
import {AppBar} from 'material-ui'
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import getMuiTheme from 'material-ui/styles/getMuiTheme'


class Header extends Component {
    static get childContextTypes() {
        return { muiTheme: React.PropTypes.object };
    }

    render() {
        return (
                <header className="header">
                <AppBar
            title="LoLProBuildJP"
                iconClassNameRight="muidocs-icon-navigation-expand-more" />
                </header>
        )
    }
}

export default Header
