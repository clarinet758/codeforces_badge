function data(){
    $.ajax({
        type: 'GET',
        url: "http://www.nowshika.com/joso/data.jsonp",
        dataType: 'jsonp',
        jsonpCallback: 'parseResponse',
        crossDomain: true,
        success: function(info){
            var i,j;
            var color = ['red','orange','violet','blue','green','gray','black'];
            var nowRating = info.rating, maxRating = info.maxRating;
            var uid = info.handle;
            var contestId    = info.contestId;
            var contestName  = info.contestName;
            var submitContestId = info.submitContestId;
            var index    = info.index;
            var problem  = submitContestId+index+" - "+info.problemName;
            var prof = "http://codeforces.com/profile/";
            var cont = "http://codeforces.com/contest/";
            $("<span>").text("(((o(*ﾟ▽ﾟ*)o)))").prependTo("#solve");
            $("<img alt='photo' class='avatar' src='http://codeforces.com/userphoto/title/"+uid+"/photo.jpg'>").prependTo("#user-avatar");

            if (nowRating >= 2200) i=0;
            else if (nowRating >= 1900) i=1;
            else if (nowRating >= 1700) i=2;
            else if (nowRating >= 1500) i=3;
            else if (nowRating >= 1200) i=4;
            else if (nowRating < 1200) i=5;

            $("<a href='"+prof+uid+"' class='"+color[i]+"' target='_parent'>").text(uid).prependTo("#handleLink");
            $("<span class='"+color[i]+"'>").text(data.rankName).prependTo("#rankName");
            $("<span class='"+color[i]+"'>").text(nowRating).prependTo("#rating");
            $("<span class='"+color[i]+"'>").text(nowRating).prependTo("#newRating");

            if (maxRating >= 2200) j=0;
            else if (maxRating >= 1900) j=1;
            else if (maxRating >= 1700) j=2;
            else if (maxRating >= 1500) j=3;
            else if (maxRating >= 1200) j=4;
            else if (maxRating < 1200) j=5;

            $("<span class='"+color[j]+"'>").text(info.maxRankName).prependTo("#maxRankName");
            $("<span class='"+color[j]+"'>").text(maxRating).prependTo("#maxRating");
            $("<span>").text(info.fluctuation).prependTo("#fluctuation");
            $("<span>").text(info.when).prependTo("#when");
            $("<a href='"+cont+contestId+"' target='_parent'>").text(info.contestName).prependTo("#contestLink");
            $("<span>").text(info.rank).prependTo("#rank");
            $("<a href='http://codeforces.com/problemset/problem/"+submitContestId+"/"+index+"' target='_parent'>").text(problem).prependTo("#problem");
            $("<span>").text(info.verdict).prependTo("#verdict");
            $("<a href='"+cont+submitContestId+"/submission/"+submitCodeId+"' target='_parent'>").text(info.submitCodeId).prependTo("#submitCodeId");
        }
    });
}
