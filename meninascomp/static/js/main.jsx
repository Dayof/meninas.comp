class TopBar extends React.Component {
    constructor(props){
      super(props);
      this.state={isHide:false};
      this.hideBar = this.hideBar.bind(this)
    }
    hideBar(){
       let {isHide} = this.state
       window.scrollY > 300?
       !isHide && this.setState({isHide:true})
       :
       isHide && this.setState({isHide:false})
    }
    componentDidMount(){
        window.addEventListener('scroll',this.hideBar);
    }
    componentWillUnmount(){
         window.removeEventListener('scroll',this.hideBar);
    }
    render(){

        let classHide=this.state.isHide?"top-bar-background":"hide"
        return <div className={classHide}></div>;
    }
}

ReactDOM.render(<TopBar/>,document.getElementById('navbar-event'));
