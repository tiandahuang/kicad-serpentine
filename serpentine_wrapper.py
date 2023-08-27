import wx
import serpentine_gui as gui
# import serpentine_utils as utils
import functools as ft

class SerpentineGUI(gui.MainFrame):

    def __init__(self, parent, validate_func, run_func):
        super(SerpentineGUI, self).__init__(parent)

        self.validate_func = validate_func
        self.run_func = run_func

        def call2(f_inner, f_outer, *args, **kwargs):
            return f_outer(f_inner(*args, **kwargs))

        self.param_getters = {
                'radius':   ft.partial(call2, self.r_value.GetValue, ft.partial(self.validate_num, lo=0)),
                'amplitude':ft.partial(call2, self.a_value.GetValue, ft.partial(self.validate_num, lo=0)),
                'alpha':    ft.partial(call2, self.alph_value.GetValue, ft.partial(self.validate_num, lo=0, hi=90)),
                'length':   ft.partial(call2, self.len_value.GetValue, ft.partial(self.validate_num, lo=0)),
                'wc':       ft.partial(call2, self.ckt_value.GetValue, ft.partial(self.validate_num, lo=1, type_conv=int)),
                'width':    ft.partial(call2, self.width_value.GetValue, ft.partial(self.validate_num, lo=0)),
                'pitch':    ft.partial(call2, self.pitch_value.GetValue, ft.partial(self.validate_num, lo=0)),
                'margin':   ft.partial(call2, self.marg_value.GetValue, ft.partial(self.validate_num, lo=0)),
        }

        self.param_setters = {
                'radius':   ft.partial(call2, str, self.r_value.SetValue),
                'amplitude':ft.partial(call2, str, self.a_value.SetValue),
                'alpha':    ft.partial(call2, str, self.alph_value.SetValue),
                'length':   ft.partial(call2, str, self.len_value.SetValue),
                'wc':       ft.partial(call2, str, self.ckt_value.SetValue),
                'width':    ft.partial(call2, str, self.width_value.SetValue),
                'pitch':    ft.partial(call2, str, self.pitch_value.SetValue),
                'margin':   ft.partial(call2, str, self.marg_value.SetValue),
        }

        self.param_defaults = {
                'radius':   1,
                'amplitude':1,
                'alpha':    0,
                'length':   10,
                'wc':       4,
                'width':    0.2,
                'pitch':    0.4,
                'margin':   0.4,
        }

        for param, val in self.param_defaults.items():
            self.param_setters[param](val)
        self.params = {param:self.param_getters[param]() for param in self.param_getters}

    # event handlers

    def RadiusParamEvent(self, event):
        self.param_event_handler(event_str)

    def AmplitudeParamEvent(self, event):
        self.param_event_handler(event_str)

    def AlphaParamEvent(self, event):
        self.param_event_handler(event_str)

    def LengthParamEvent(self, event):
        self.param_event_handler(event_str)

    def WirePitchParamEvent(self, event):
        self.param_event_handler(event_str)

    def EdgeDisableParamEvent(self, event):
        self.param_event_handler(event_str)

    def FWCParamEvent(self, event):
        self.param_event_handler(event_str)

    def FWidthParamEvent(self, event):
        self.param_event_handler(event_str)

    def BWCParamEvent(self, event):
        self.param_event_handler(event_str)

    def BWidthParamEvent(self, event):
        self.param_event_handler(event_str)

    def ApplyEvent(self, event):
        self.param_event_handler(event_str)

    def CancelEvent(self, event):
        self.param_event_handler(event_str)

    def ValidateEvent(self, event):
        self.param_event_handler(event_str)

    def ApplyEvent(self, event):
        event_str = 'apply'
        self.log(event_str)
        if not self.validate_func(self.params):
            pass    # display warning or something
        self.run_func(self.params)
        wx.Exit()

    def CancelEvent(self, event):
        event_str = 'cancel'
        self.log(event_str)
        wx.Exit()

    def ValidateEvent(self, event):
        event_str = 'validate'
        self.log(str(self.params))
        status, errmsg = self.validate_func(self.params)
        if not status:
            self.error(errmsg)

    # helper methods

    def log(self, t):
        self.StatusBar.SetStatusText(t)
    
    def error(self, t):
        frame = self.SerpentineError(self, t)
        frame.Show(True)

    def param_event_handler(self, event_str):
        val = self.param_getters[event_str]()
        if val:
            self.params[event_str] = val
        else:
            self.param_setters[event_str](self.params[event_str])
        self.log(f'{event_str} set to {self.params[event_str]}')

    @staticmethod
    def validate_num(val, lo=None, hi=None, clip=False, type_conv=float):
        try:
            f = type_conv(val)
        except ValueError as e:
            return None

        if lo is not None or hi is not None:
            if lo is None: lo = -float('inf')
            if hi is None: hi = float('inf')
            if clip:
                f = type_conv(min(max(f, lo), hi))
            else:
                if f > hi or f < lo:
                    return None
        
        return f
    
    class SerpentineError(gui.ErrorDialog):

        def __init__(self, parent, text):
            super(SerpentineGUI.SerpentineError, self).__init__(parent)
            self.text = text
            self.text_width = 0

        def ResizeEvent(self, event):
            new_width = self.GetSize().width
            if abs(self.text_width - new_width) > 20:
                self.message.SetLabel(self.text)
                self.text_width = new_width
            self.message.Wrap(new_width - 20)

        def ValidateEvent(self, event):
            self.Destroy()


class SerpentineWrapper():

    def __init__(self):
        app = wx.App(False)
        frame = SerpentineGUI(None, self.validate, self.run)
        frame.Show(True)
        app.MainLoop()

    @staticmethod
    def validate(a):
        print(a)
        return True, None
    
    @staticmethod
    def run(a):
        print(a)
        return True, None

if __name__ == '__main__':

    SerpentineWrapper()



# TODO: remove separate wire-to-wire and wire-to-edge
# TODO: separate top/bottom spacing and widths
# TODO: disable edgecuts
