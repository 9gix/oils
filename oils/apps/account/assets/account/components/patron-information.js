import React, { Component } from 'react'


class PatronInformation extends Component {
    constructor(props){
        super(props)
    }

    render(){
        let { patron } = this.props
        if (Object.keys(patron).length === 0) return null

        return (
            <div>
              <dl>
                <dt>Name</dt>
                <dd>{ patron.name }</dd>
                <dt>Address</dt>
                <dd>{ patron.address }</dd>
                <dd>{ patron.country }</dd>
                <dd>{ patron.postcode }</dd>
                <dt>Contact</dt>
                <dd>{ patron.contact }</dd>
                <dt>Note</dt>
                <dd>{ patron.note }</dd>
                <dt>Loan Duration</dt>
                <dd>{ patron.loan_duration } days</dd>
                <dt>Renewal Limit</dt>
                <dd>{ patron.renewal_limit }</dd>
                <dt>Current Loan</dt>
                <dd>--</dd>
                <dt>Max Loan</dt>
                <dd>{ patron.loan_limit }</dd>
              </dl>
            </div>
        )
    }
}

export { PatronInformation }
