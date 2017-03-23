import React from 'react'
import {render} from 'react-dom'
import {createStore} from 'redux'
import {Provider} from 'react-redux'
import Champions from './champions/champions.js'
import reducer from './reducer.js'

const store = createStore(reducer)

window.onload = function () {
    render(
            <Provider store={store}>
            <Champions />
            </Provider>,
        document.getElementById('root')
    )
}
