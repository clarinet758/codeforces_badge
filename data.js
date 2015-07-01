function data(){
    $.ajax({
        type: 'GET',
        url: "http://www.nowshika.com/joso/data.jsonp",
        dataType: 'jsonp',
        jsonpCallback: 'parseResponse',
        crossDomain: true,
        success: function(info){
            var color = ['red','orange','violet','blue','green','gray','black'];
            var nowRating = info.rating, maxRating = info.maxRating;
            var uid = info.handle;
            var contestId    = info.contestId;
            var contestName  = info.contestName;
            var submitCodeId = info.submitCodeId;
            var submitContestId = info.submitContestId;
            var index    = info.index;
            var problem  = submitContestId+index+" - "+info.problemName;
            var prof = "http://codeforces.com/profile/";
            var cont = "http://codeforces.com/contest/";
            $("<span>").text("(((o(*ﾟ▽ﾟ*)o)))").prependTo("#solve");
            $("<img alt='photo' class='avatar' src='http://codeforces.com/userphoto/title/"+uid+"/photo.jpg'>").prependTo("#user-avatar");
            function flag(x){
                var y;
                if (x >= 2200) y=0;
                else if (x >= 1900) y=1;
                else if (x >= 1700) y=2;
                else if (x >= 1500) y=3;
                else if (x >= 1200) y=4;
                else if (x < 1200) y=5;

                return y;
            }

            var i = flag(nowRating);
            $("<a href='"+prof+uid+"' class='"+color[i]+"' target='_parent'>").text(uid).prependTo("#handleLink");
            $("<span class='"+color[i]+"'>").text(info.rankName).prependTo("#rankName");
            $("<span class='"+color[i]+"'>").text(nowRating).prependTo("#rating");
            $("<span class='"+color[i]+"'>").text(nowRating).prependTo("#newRating");

            var j = flag(maxRating);
            $("<span class='"+color[j]+"'>").text(info.maxRankName).prependTo("#maxRankName");
            $("<span class='"+color[j]+"'>").text(maxRating).prependTo("#maxRating");
            $("<span>").text(info.fluctuation).prependTo("#fluctuation");
            $("<span>").text(info.when).prependTo("#when");
            $("<a href='"+cont+contestId+"' target='_parent'>").text(info.contestName).prependTo("#contestLink");
            $("<span>").text(info.rank).prependTo("#rank");
            $("<a href='http://codeforces.com/problemset/problem/"+submitContestId+"/"+index+"' target='_parent'>").text(problem).prependTo("#problem");
            if (info.verdict==="Accepted") $("<span class='AC'>").text(info.verdict).prependTo("#verdict");
            else $("<span>").text(info.verdict).prependTo("#verdict");
            $("<a href='"+cont+submitContestId+"/submission/"+submitCodeId+"' target='_parent'>").text(info.submitCodeId).prependTo("#submitCodeId");
        }
    });
}
