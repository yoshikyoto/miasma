import {combineReducers} from 'redux'
import championsReducer from './champions/reducer.js'
import newsReducer from './reducers/news.js'


export default combineReducers({
    championsReducer,
    newsReducer,
});
