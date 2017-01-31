(function (e) {
	e.extend(e.ui.tabs.prototype, {
		rotation: null,
		rotationDelay: null,
		continuing: null,
		rotate: function (n, r) {
			var i = this,
			s = this.options;
			if ((n > 1 || i.rotationDelay === null) && n !== undefined) {
				i.rotationDelay = n
			}
			if (r !== undefined) {
				i.continuing = r
			}
			var o = i._rotate || (i._rotate = function (e) {
				clearTimeout(i.rotation);
				i.rotation = setTimeout(function () {
					var e = s.active;
					i.option("active", ++e < i.anchors.length ? e: 0)
				},
				n);
				if (e) {
					e.stopPropagation()
				}
			});
			var u = i._unrotate || (i._unrotate = !r ?
			function (e) {
				if (e.clientX) {
					i.rotate(null)
				}
			}: function (e) {
				t = s.active;
				o()
			});
			if (n) {
				this.element.bind("tabsactivate", o);
				this.anchors.bind(s.event + ".tabs", e.proxy(i.unpause, i));
				o()
			} else {
				clearTimeout(i.rotation);
				this.element.unbind("tabsactivate", o);
				this.anchors.unbind(s.event + ".tabs", e.proxy(i.pause, i));
				delete this._rotate;
				delete this._unrotate
			}
			if (n === 1) {
				n = i.rotationDelay
			}
			return this
		},
		pause: function () {
			var e = this,
			t = this.options;
			e.rotate(0)
		},
		unpause: function () {
			var e = this,
			t = this.options;
			e.rotate(1, e.continuing)
		}
	})
})(jQuery);
$(function () {
	$("#featured_slide").tabs({
		fx: {
			opacity: "show"
		}
	}).tabs("rotate", 6000)
})
