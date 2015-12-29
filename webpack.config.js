module.exports = {

    entry: {
        main: "./asset/main",
        circulation_issue: "./asset/circulation/issue"
    },
    output: {
        path: __dirname + '/static/',
        filename: "[name].js"
    },
    module: {
        loaders: [
            {
                test: /\.less$/,
                loader: "style-loader!css-loader!less-loader"
            },
            {
                test: /\.jsx?$/,
                exclude: /(node_modules|bower_components)/,
                loader: 'babel',
                query: {
                    presets: ['react', 'es2015']
                }
            }
        ]
    }
}
