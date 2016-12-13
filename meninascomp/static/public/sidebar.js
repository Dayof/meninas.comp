"use strict";

var App = React.createClass({
    displayName: "App",

    showRight: function showRight() {
        this.refs.right.show();
    },

    render: function render() {
        return React.createElement(
            "div",
            null,
            React.createElement(
                "button",
                { onClick: this.showRight, type: "button", "class": "navbar-button" },
                "OLAR"
            ),
            React.createElement(
                Menu,
                { ref: "right", alignment: "right" },
                React.createElement(
                    "a",
                    { href: ".." },
                    "First Page"
                ),
                React.createElement(
                    "a",
                    { href: ".." },
                    "Second Page"
                ),
                React.createElement(
                    "a",
                    { href: ".." },
                    "Third Page"
                )
            )
        );
    }
});

var Menu = React.createClass({
    displayName: "Menu",

    getInitialState: function getInitialState() {
        return {
            visible: false
        };
    },

    show: function show() {
        this.setState({ visible: true });
        document.addEventListener("click", this.hide.bind(this));
    },

    hide: function hide() {
        document.removeEventListener("click", this.hide.bind(this));
        this.setState({ visible: false });
    },

    render: function render() {
        return React.createElement(
            "div",
            { className: "menu" },
            React.createElement(
                "div",
                { className: (this.state.visible ? "visible " : "") + this.props.alignment },
                this.props.children
            )
        );
    }
});

ReactDOM.render(React.createElement(App, null), document.getElementById('sidebar'));