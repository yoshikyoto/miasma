import React, {Component} from 'react';
import {connect} from 'react-redux';
import {Toolbar, ToolbarTitle} from 'material-ui/Toolbar';
import {Table, TableBody, TableRow, TableRowColumn} from 'material-ui/Table';
import Axios from 'axios';
import {renderAllNews} from '../../reducers/news.js';

/** ニュース */
class News extends Component {
    render() {
        if(this.props.news.length <= 0) {
            this.getNews();
        }
        
        return (
            <div>
            <Toolbar>
            <ToolbarTitle text="LoL・LJLニュース" />
            </Toolbar>
            <Table height={240} selectable={false}
            style={{
                width: 800,
                marginLeft: 'auto',
                marginRight: 'auto',
            }}>
            <TableBody displayRowCheckbox={false}>
            {this.props.news.map((item) => {
                return (
                    <TableRow>
                    <TableRowColumn style={{width: 100}}>{item.date}</TableRowColumn>
                    <TableRowColumn>
                    <a href={item.link}>
                    {item.text}
                    </a>
                    </TableRowColumn>
                    </TableRow>
                )
            })}
            </TableBody>
            </Table>
            </div>
        );
    }

    getNews() {
        Axios.get('/api/v1/news.json').then(response => {
            this.props.renderAllNews(response.data.data);
        });
    }
}

function mapStateToProps(state) {
    return {
        news: state.newsReducer.news
    };
}

function mapDispatchToProps(dispatch) {
    return {
        renderAllNews: (news) => {
            dispatch(renderAllNews(news))
        },
    };
}

export default connect(mapStateToProps, mapDispatchToProps)(News);
