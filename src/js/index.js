import React from 'react'
import {render} from 'react-dom'
import {createStore} from 'redux'
import {Provider} from 'react-redux'
import injectTapEventPlugin from 'react-tap-event-plugin'
import darkBaseTheme from 'material-ui/styles/baseThemes/darkBaseTheme'
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider'
import Champions from './champions/champions.js'
import reducer from './reducer.js'
import Header from './header/header.js'
import News from './components/news/news.js'

/** reactでtapイベントを取るのに必要らしい */
injectTapEventPlugin()
const store = createStore(reducer)


window.onload = function () {
    render(
        <MuiThemeProvider>
          <Provider store={store}>
            <div>
              <Header />
              <News />
              <Champions />
            </div>
          </Provider>
        </MuiThemeProvider>,
        document.getElementById('root')
    )
}
