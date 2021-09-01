import React, { Component } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import { getBooks } from "./BookTypes";

import Book from "./Book";

class BookList extends Component {
    componentDidMount() {
        this.props.getBooks();
    }

    render() {
        const books = this.props;

        if (books.length === 0) {
            return <h2> Please add your first book </h2>;
        }

        /*
        let items = books.map(book => {
            return <Book key={book.id} book={book} />;
        });
        */

        return (
            <div>
                <h2>Books</h2>
                {books}
            </div>
        );
    }
}

BookList.propTypes = {
    getBooks: PropTypes.func.isRequired,
    books: PropTypes.object.isRequired
};

const mapStateToProps = state => ({
    books: state.notes
});

export default connect(mapStateToProps, {
    getBooks
})(withRouter(BookList));

export { BookList};