import wx
from .serpentine_gui import MainFrame, ErrorDialog
from .serpentine_utils import SerpentineVector
import functools as ft
import os

class SerpentineGUI(MainFrame):

    def __init__(self, parent, validate_func, run_func):
        super(SerpentineGUI, self).__init__(parent)

        self.validate_func = validate_func
        self.run_func = run_func

        def call2(f_inner, f_outer, *args, **kwargs):
            return f_outer(f_inner(*args, **kwargs))
        
        def wx_textctrl_getvalue(wx_obj, **validate_kwargs):
            return ft.partial(call2, 
                              wx_obj.GetValue, 
                              ft.partial(self.validate_num, **validate_kwargs))

        def wx_textctrl_setvalue(wx_obj):
            return ft.partial(call2, str, wx_obj.SetValue)


        self.param_getters = {
                'radius':   wx_textctrl_getvalue(self.r_value, lo=0),
                'amplitude':wx_textctrl_getvalue(self.a_value, lo=0),
                'alpha':    wx_textctrl_getvalue(self.alph_value, lo=-90, hi=90),
                'length':   wx_textctrl_getvalue(self.len_value, lo=0),
                'pitch':    wx_textctrl_getvalue(self.pitch_value, lo=0),
                'f_wc':     wx_textctrl_getvalue(self.f_wc_value, lo=0, type_conv=int),
                'f_width':  wx_textctrl_getvalue(self.f_width_value, lo=0),
                'b_wc':     wx_textctrl_getvalue(self.b_wc_value, lo=0, type_conv=int),
                'b_width':  wx_textctrl_getvalue(self.b_width_value, lo=0),
                'noedge':   self.edgedisable_value.GetValue,
        }

        self.param_setters = {
                'radius':   wx_textctrl_setvalue(self.r_value),
                'amplitude':wx_textctrl_setvalue(self.a_value),
                'alpha':    wx_textctrl_setvalue(self.alph_value),
                'length':   wx_textctrl_setvalue(self.len_value),
                'pitch':    wx_textctrl_setvalue(self.pitch_value),
                'f_wc':     wx_textctrl_setvalue(self.f_wc_value),
                'f_width':  wx_textctrl_setvalue(self.f_width_value),
                'b_wc':     wx_textctrl_setvalue(self.b_wc_value),
                'b_width':  wx_textctrl_setvalue(self.b_width_value),
                'noedge':   self.edgedisable_value.SetValue,
        }

        self.params = {param:None for param in self.param_getters}

    # event handlers

    def ApplyEvent(self, event):
        status, errmsg = self.get_all_params()
        if not status:
            self.error(errmsg)
            return
        status, errmsg = self.run_func(self.params)
        if not status:
            self.error(errmsg)
            return
        self.Destroy()

    def CancelEvent(self, event):
        self.Destroy()

    def ValidateEvent(self, event):
        status, errmsg = self.get_all_params()
        if not status:
            self.error(errmsg)
            return
        status, errmsg = self.validate_func(self.params)
        if not status:
            self.error(errmsg)
        self.error('\n'.join([f'{p}:{v}' for p, v in self.params.items()]))

    # helper methods

    def get_all_params(self):
        params = {param:self.param_getters[param]() for param in self.param_getters}
        invalid = []
        for param, val in params.items():
            if val is not None: 
                self.params[param] = val
            else:
                self.param_setters[param]('')
                invalid.append(param)
        errmsg = '\n'.join([f'{p} parameter has invalid value' for p in invalid])
        return (len(invalid) == 0), errmsg

    def log(self, t):
        self.StatusBar.SetStatusText(t)
    
    def error(self, t):
        frame = self.SerpentineError(self, t)
        frame.Show(True)
    

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
    
    class SerpentineError(ErrorDialog):

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

        cd = os.getcwd()        # weird hack to make loading the images work.
        os.chdir(os.path.dirname(__file__))
        frame = SerpentineGUI(None, self.validate, self.run)
        os.chdir(cd)

        frame.Show(True)
        app.MainLoop()

    @staticmethod
    def validate(args):
        return SerpentineVector().validate(args)
    
    @staticmethod
    def run(args):
        return SerpentineVector().run(args)

if __name__ == '__main__':

    SerpentineWrapper()
